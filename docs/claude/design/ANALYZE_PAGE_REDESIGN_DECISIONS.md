# Analyze Page Redesign — Decision Log

> **Status:** Design complete for 17 items (13 original + 4 resolved this
>            round). Open items tracked in §9. **No application code has been
>            changed.** Implementation plan at §7, not yet executed — this
>            remains a design-only deliverable until a future session is
>            explicitly asked to build it.
> **Created:** Day 109
> **Process record:** `/Users/balajik/.claude/plans/agile-giggling-hoare.md`
>            (the plan file is a session-scoped process log; this file is the
>            durable decision record and should be updated in place going
>            forward, not superseded by a new plan file)
> **Decision lens:** `docs/claude/stable/PERSONA.md` (Golden Rule 34) — every
>            Engine/Info split below was tested against Core Principle 1
>            (capital preservation before growth) and the behavioral-finance
>            pitfalls list, not just against the user's initial framing.
> **Freeze status:** Freeze-independent display work — same category as Days
>            93/101/103/105/106/108 (`ROADMAP.md`). **Zero changes to any of
>            the 4 live forward-test tracks' logic.** See §8 for the file-by-
>            file audit that makes this claim checkable, not just asserted.
> **Implementation:** Phase 0 of the Day 119 plan done Day 121 (§6/§9 copy
>            corrections — see §10). Build from
>            `ANALYZE_PAGE_REDESIGN_IMPLEMENTATION_PLAN_DAY119.md`, not §7.
> **Last Updated:** Day 121

---

## §0 — First principles: what moves and what doesn't

The user's own framing, verbatim, is the governing bar for every decision
below: *"i am not saying to eliminate things all i am saying is, to change
few things to info for human decisions and few things in the engine to
decide."* And, on why now rather than trusting the original mechanical
design outright: *"even though 100 years trading principles existed, in AI
era leave few things to human judgement, else it will become too noise."*

Tested against pushback (should the market-regime gate go informational
too?), the bar that survived is:

> **Mechanize what's proven reliable in this specific implementation and
> governs a moment humans are behaviorally bad at (stops, regime blindness,
> sizing after a loss). Leave to human judgment what's currently unreliable
> in this implementation, or requires synthesizing messy context a fixed
> formula was never going to do well.**

This is not "trust the machine less across the board." Fundamentals, R:R,
and position sizing move to informational because each has a *specific,
documented reliability problem in this codebase* (a 40% live/backtest data
mismatch; a years-long live/backtest R:R divergence and an extreme-vs-
nearest S&R selection bug; a hardcoded fake position-size label). Market
regime and core technical structure stay mechanical because both are
backtest-validated, JS/Python parity-tested, and — in regime's case —
protecting against exactly the moment (a real drawdown) humans are worst at
trusting their own judgment.

### What this IS / IS NOT

| This redesign IS | This redesign IS NOT |
|---|---|
| A change to what the Analyze page *asserts* to the user | A change to any backtested threshold, formula, or validated computation |
| A change to which computed values are *displayed* vs. *gated on* | A change to `determineVerdict()`, `categorical_engine.py`, or any parity-tested function's behavior |
| A change to the *default view* the user lands on | A change to the Simple Checklist's own 9-criterion logic |
| A change to 2 utility files (`riskRewardCalc.js`, `positionSizing.js`) and `App.jsx`'s display layer | A change to any file under `backend/paper_trading/`, `backend/support_resistance.py`, or `backend/backtest/categorical_engine.py` |
| Freeze-independent (per the Day 93/101/103/105/106/108 precedent) | An exception to the freeze — it changes nothing about the 4 live tracks |

---

## §1 — Hard constraints (read before touching anything)

These four are non-negotiable and structural, not judgment calls:

1. **`assessTechnical()`, `assessFundamental()`, `assessSentiment()`,
   `assessRiskMacro()`, and `determineVerdict()` keep their exact export
   names, signatures, and behavior, unmodified.** `frontend/scripts/
   verdict_grid.mjs:21-25` imports them by name for the JS/Python parity
   grid test (Golden Rule 19, 86,400 combos). Any signature or behavior
   change breaks that contract.
2. **`backend/support_resistance.py` is not edited, at all.**
   `backend/paper_trading/live_signals.py:45` imports `compute_sr_levels`;
   `:167-168` reads `sr_levels.meta['trade_viability']['viable']`; `:191`
   gates a real, currently-open **Path B** signal on it
   (`passes = is_viable and rr_ratio >= MIN_RR`). This function is load-
   bearing for a live forward-test track at ~44/100 trades. The frontend
   redesign *stops reading* two of its output fields (`position_size_advice`,
   `risk_reward_context`) — the backend keeps producing them unchanged.
3. **`backend/backtest/categorical_engine.py` is not edited.** It is the
   Python half of the parity contract and is imported directly by
   `live_signals.py:47` (`from backtest.categorical_engine import
   run_assessment`), which gates the live **momentum tracks'** (Path A and
   Path B) real entries on `determine_verdict()`'s output — including the
   Fundamental assessment. **This means Fundamentals will keep gating real,
   live trade entries after this redesign ships**, even though the Analyze
   page will no longer present Fundamentals as a gate to the human reading
   it. That is intentional and correct — the live tracks are frozen and a
   logic change would reset their trade count — but it is a genuine
   UI-says-vs-system-does gap and must stay disclosed here, not left
   implicit (same discipline as Golden Rule 38's "an undocumented second
   meaning is the risk, not the reuse itself").
4. **No threshold anywhere in the verdict tree, the Simple Checklist, or the
   S&R engine changes value.** Every number this redesign surfaces
   differently (ADX 20, R:R 1.0/1.2/2.0, the fundamentals bands) is an
   *existing*, already-used number — reused for display purposes, never
   re-tuned. Per Golden Rule 18/20: a display change is not a re-test.

---

## §2 — Component decision register

Each entry: Question → Research (file:line, verified this session) →
Reasoning (PERSONA lens) → Decision → What this does NOT change → Status.

### 1. Trend Template / RSI / RS Rating
**Question:** Should the core technical structure signal stay mechanical?
**Research:** `categoricalAssessment.js:207-318` (`assessTechnical()`) reads
exactly three inputs — `trendTemplate.criteria_met`, RSI, and
`technicalData.rsData.rs52Week`. Strong = TT≥7/8 AND RSI 50-70 AND RS≥1.0.
Parity-covered: `test_verdict_parity.py` grids TT×RSI×RS×ADX×VIX×SPY×
fundamentals×holding-period = 86,400 combos, all passing as of the Day 108
audit.
**Reasoning:** Backtest-validated (Gates G1-G9), deterministic math off price
data the app already trusts. No external-data reliability problem exists
here — the opposite of the Fundamentals situation.
**Decision:** **Engine** — drives the Technical Read directly.
**What this does NOT change:** `assessTechnical()` itself, its thresholds,
or its parity coverage.
**Refinement:** `assessTechnical()` collapses two different situations into
one `Weak` result — pattern-detection failure (`:274-275`) and a genuine
Stage-4 decline both render identically. The Technical Read display needs a
4th state, `Unavailable`, added as a **display-layer branch** (checking the
already-exported `technical.data.trendTemplateAvailable === false`), not a
change to `assessTechnical()` itself.
**Status:** Locked.

---

### 2. ADX — as a modifier on the Technical Read
**Question:** Does ADX belong in the "read," and if so, how, given it isn't
currently part of `assessTechnical()` at all?
**Research:** Confirmed by reading the full function: `assessTechnical()`
never references ADX. The Python mirror's own docstring states it plainly
(`categorical_engine.py:47`: *"adx: ADX value (stored in data, not used for
assessment)"*). ADX's only mechanical role today is inside
`determineVerdict()` — `:777-786`, `if (adxValue < 20 && strongCount >= 2)
return HOLD`.
**Reasoning:** Under a naive "Technical Read = `assessTechnical()` output"
design, this mechanical caution would silently vanish from the page — a
stock with Trend Template 8/8, RSI 62, RS 1.1, and ADX 14 (no confirmed
trend) would show "Technical Read: Strong" with no signal that the trend
isn't actually confirmed yet.
**Decision:** **Engine** — ADX<20 appends a visible modifier to the Technical
Read chip: *"Technical Read: Strong · trend not yet confirmed (ADX 14.2)."*
Implemented as a **new, additive display function**
(`deriveTechnicalRead()`), never inside `assessTechnical()` or
`determineVerdict()` — so parity is untouched. The 20 threshold is not new;
it's the same number already used in `determineVerdict():777`,
`simplifiedScoring.js:242`, and the position-size ladder.
**What this does NOT change:** `assessTechnical()`'s signature/output,
parity coverage, or the 20 threshold's value anywhere else it's used.
**Status:** Locked (resolved via AskUserQuestion, Recommended option taken).

---

### 3. ADX — as a position-size trigger
**Question:** Should ADX continue to drive an automatic position-size
recommendation?
**Research:** The card currently carries **three mutually inconsistent ADX
interpretations simultaneously**: the ADX chip tooltip (`App.jsx:1727`, "≥25
= Pullback preferred / <25 = Momentum suggested"), the Position row tooltip
(`:1884`, "Full = ADX 25+, Reduced = 20-25, Wait = <20"), and the Reason text
(`:1893-1900`, ADX≥30 → "momentum entry viable" — the *opposite* mapping of
the chip tooltip). `determineVerdict():704-728` uses a *fourth* mapping.
**Reasoning:** Reducing ADX to a raw, undecorated number resolves all four
contradictions by construction — there's no longer a "which mapping is
right" question because none of them are displayed as a recommendation.
**Decision:** **Info** — raw stat only, shown in the Sizing Inputs grid
(§6), no label, no threshold-based recommendation.
**What this does NOT change:** ADX's computation; its use in the Technical
Read modifier (item 2, a different, retained use).
**Status:** Locked.

---

### 4. Market Regime (VIX + SPY vs. 200-day SMA)
**Question:** Should the regime gate go informational along with everything
else?
**Research:** `assessRiskMacro()` (`categoricalAssessment.js:551-623`) is
clean and fully parity-mirrored, including the Day-57 early-bear 50-SMA cap
(`:609-615`). Its only current mechanical effect is
`determineVerdict():758-760`: `if (riskMacro === 'Unfavorable') return
HOLD`. Everything else about regime on the page today is de-emphasized: a
1-letter chip (`App.jsx:1470-1472`), a tile inside the collapsed-by-default
Assessment Breakdown, and `RegimeBanner.jsx` (Context-tab only, measures a
different macro composite entirely — confirmed via grep, zero references in
`App.jsx`).
**Reasoning:** Persona Core Principle 1 — capital preservation before
growth. This is the one guardrail in the whole system that's actually
protecting the user from themselves in a real drawdown; softening it would
remove the discipline humans are worst at holding onto under loss aversion
and euphoria. This should stay mechanical *and become more visible*, not
less.
**Decision:** **Engine** — hard gate, unchanged in mechanism. **New:** a
dedicated, always-visible **Regime band** (not a collapsible chip) at the
top of the page, present in all three states (Favorable/Neutral/
Unfavorable), carrying language directly from `assessRiskMacro().reasons`.
This is the one deliberate exception to the "nothing gates" rule on this
page, and it says so in its own copy (§6).
**What this does NOT change:** `assessRiskMacro()`'s thresholds or the
early-bear cap logic.
**Status:** ~~Locked — split from the composite verdict badge into its own
element (resolved via AskUserQuestion, Recommended option: "Split into two
elements").~~ **REVISED Day 110 — see below.**

**Revision (Day 110):** The user directly challenged the hard-gate framing
("I will deal with regime and sector, why do you worry to put it in as a
hard gate"). Re-examined rather than defended: under this same redesign,
"hard gate" had already shrunk to something narrower than the label implied
— item 12 makes the Technical Read never suppressed or grayed out by
regime, so nothing on the page actually blocks the user from acting; the
only remaining "gate" content was a non-collapsible banner using imperative
language ("stand-down regime... deliberately not left to judgment") plus
`determineVerdict()` still computing an internal HOLD nothing on the page
displays. Tested against Persona Core Principle 1 a second time with the
user's actual counter-evidence on the table (9 months of real, live
judgment on this exact tool, explicit ownership of regime/sector risk in
their own process) rather than an abstract "humans are bad at this" prior —
the counter-evidence wins. **Decision reversed: Regime becomes Info, same
treatment as Fundamentals/R:R/Sizing — no enforcement language, no
non-collapsible banner.** One asymmetry kept, not as a gate but as a
default-visibility choice: regime is portfolio-wide (affects every open
position at once) where Fundamentals is idiosyncratic (affects one stock) —
so it stays expanded by default rather than collapsed like Sentiment, but
that's a display default, not a rule the page enforces. Explicitly
confirmed this only touches the Analyze page's display — the **live
momentum tracks' actual entry gate keeps regime wired into
`categorical_engine.py`/`live_signals.py` unchanged**, per §1 constraint 3;
nothing here proposes touching that. New PERSONA.md Feedback Log entry
(Day 110) — logs the persona genuinely reversing a locked position under a
good counter-argument, not just holding or folding on request.
**Known inconsistency, not yet fixed:** the published mockup
(`docs/claude/design/mockups/analyze_page_redesign_mockup.html`) still
shows the old "stand-down" banner language — not updated this session,
pending user confirmation.

---

### 5. Fundamentals (ROE / Revenue Growth / Debt-Equity)
**Question:** Should Fundamentals count toward the verdict?
**Research:** `KNOWN_ISSUES_DAY108.md:89-91` (carried from Day 78/79,
originally measured Day 92): **40.0% disagreement rate** between live
(Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly)
Fundamental labels, measured on 20 liquid tickers — **revenue growth is the
dominant driver**. Open, unmitigated.
**Reasoning:** The diagnosis is a *data reliability* problem, not evidence
that fundamentals don't matter to a swing decision — for a "Position"
(1-3 month) hold, real fundamental deterioration is a real risk a clean
chart won't show. The fix is to stop scoring it as a precise 3-tier input
(fragile to 40% noise) and use it as a binary red-flag screen instead (more
robust to noisy data), not to discard the signal.
**Decision:** **Info** — becomes a binary red-flag screen (thresholds in
§5/§6), displayed gray (never colored as a verdict), fully separated from
the Technical Read.
**Precise scope — do not conflate with a code change:** Under Option A
(item 12), **`determineVerdict()` itself is not modified.**
`categoricalAssessment.js:689-690` still computes `strongCount` from
`[technical, fundamental]` internally — Fundamentals technically remain
part of that internal calculation. **What actually changes is that
`determineVerdict()`'s composite output stops being displayed as the page's
headline.** This distinction matters: a future session reading "fundamentals
excluded from strongCount" and going to actually remove it from that array
would be editing a parity-tested function for no reason and risking Golden
Rule 19 breakage. The correct mental model is "the composite verdict is no
longer shown," not "fundamentals no longer feed it internally."
**What this does NOT change:** `assessFundamental()`'s scoring bands (kept
as-is for their original purpose — see item 5 is about *display*, item 5's
thresholds question is answered separately in §5); `determineVerdict()`'s
internal computation; the live momentum tracks' entry gate (§1, constraint
3).
**Status:** Locked (wording corrected this round — see §3).

---

### 6. Sentiment (Fear & Greed)
**Question:** Any change needed?
**Research:** Already correctly informational since Day 70 —
`determineVerdict():689` counts only `[technical, fundamental]`; the tile
(`App.jsx:2381-2387`) already carries `infoLabel="(info)"`, `opacityMuted`,
and a sentiment-specific gray-not-yellow Neutral color.
**Reasoning:** This is the existing reference implementation the redesign
extends to Fundamentals. No change needed to the mechanism.
**Decision:** **Info**, unchanged.
**Refinement:** `assessSentiment():463-470` silently returns `'Neutral'`
with reason "data unavailable - defaulting to neutral" on fetch failure —
the exact silent-fallback shape `GOLDEN_RULES.md` names explicitly ("VIX=20
on failure, F&G=50 on error mask real problems," Day 54). The card should
distinguish **"Neutral (F&G 47)"** from **"Unavailable."** The field
(`data.rating: 'Unavailable'`) already exists at `:468` — display-layer fix
only.
**What this does NOT change:** `assessSentiment()`'s exclusion from
`strongCount`, its thresholds.
**Status:** Locked.

---

### 7. Risk:Reward
**Question:** Should R:R gate the display?
**Research (corrected this round — see §3 for what was wrong before):**
There are **4 different R:R formulas** in the app, not "3 different
thresholds" (that framing re-opened an already-closed finding —
`KNOWN_ISSUES_DAY108.md:8` explicitly closed the 3-thresholds question as
"clarified, not a bug"). The real, verified problem — see the full table in
§4 — is that two structurally different formulas both print on the Trade
Setup card within 200 lines of each other, one of which ("R:R Context") is a
ratio of percentage distances with no stop or ATR at all, answering a
different question under the same label. Separately, two real open bugs feed
into every R:R shown: the pivot S&R method selects the most extreme level in
range, not the nearest one (`support_resistance.py:1049-1051`, open Medium,
`KNOWN_ISSUES_DAY108.md:32-37`), and Golden Rule 35 documents the live R:R
gate going years without matching its own backtest.
**Reasoning:** A number built on plumbing with these specific, documented
cracks shouldn't get to visually suppress a setup by graying it out. Persona
Core Principle 5 (skepticism scales with how good/authoritative a number
looks) applies directly.
**Decision:** **Info** — shown as a plain gray number, no color ramp, no
viability gate, no "NOT VIABLE" badge, no panel suppression.
**What this does NOT change:** The underlying `calculateRiskReward()`
arithmetic (item 8) — only its *display treatment*.
**Status:** Locked (reasoning corrected this round).

---

### 8. Entry / Stop / Target price computation
**Question:** Should the raw arithmetic stay automated?
**Research:** `riskRewardCalc.js:22-61` — ATR-based stops, nearest S/R for
entry/target. Confirmed the same arithmetic is implemented a second time,
independently, in `backend.py:1664-1684` — the two agree today only because
both consume the same `srData` inputs, not because anything enforces
agreement (a smaller instance of the Golden Rule 19/35 shape).
**Reasoning:** Computing the raw levels automatically is not the problem —
interpreting whether the resulting R:R is acceptable is what moves to the
human (item 7).
**Decision:** **Engine** — the arithmetic itself stays automated.
**What this does NOT change:** Nothing changes here; this item exists to
draw the line clearly against item 7.
**Note, not a decision:** The backend/frontend duplicate formula is a real,
pre-existing DRY gap (Code Architecture Rule 7). Not fixed here — recorded
as a post-freeze pointer, since fixing it would mean editing
`backend.py`'s S&R route, which feeds `compute_sr_levels` (constraint 2).
**Status:** Locked.

---

### 9. Position size label (FULL / HALF / REDUCED)
**Question:** Should the app keep issuing a prescriptive size label?
**Research:** Three sources, not the two originally reported — precise
listing matters for the implementation plan:
1. `App.jsx:1884-1889` — Pullback panel, ADX-derived `full/reduced/wait`.
2. `App.jsx:1939-1940` — Momentum panel, **hardcoded `half`** — literally
   `<span className="text-yellow-400">half</span>` with zero computation
   behind it, confirmed by direct read, on screen since Day 39 (60+ days).
3. `App.jsx:1699-1704` — `srData.meta.tradeViability.position_size_advice`,
   computed server-side (`support_resistance.py:449/457/465/473`) from
   *support distance*, an entirely different basis from source 1. This
   source is also conditionally suppressed by a condition
   (`categoricalResult?.verdict?.verdict !== 'AVOID'`) that reads the
   composite verdict item 12 is removing from display — **it becomes
   orphaned logic the moment the verdict badge disappears** and must be
   explicitly deleted, not left dangling (Golden Rule 32's "what else calls
   the thing I changed" lens).
All three can render simultaneously and disagree.
**Reasoning:** Van Tharp — position sizing is ~90% of a system's results
(Persona Core Principle 2). Too consequential for an automated label,
especially proven by source 2's total fabrication.
**Decision:** **Info** — the `Position` row is deleted from both entry
panels entirely; replaced by a shared "Sizing inputs" stat grid (raw ADX,
ATR, stop-distance %, RVOL, VIX) plus unconditional CTAs to the existing
Position Size Calculator.
**What this does NOT change:** `backend/support_resistance.py`'s
`assess_trade_viability()` function itself (constraint 2) — it keeps
computing and returning `position_size_advice`; the frontend simply stops
reading that field.
**Status:** Locked.

---

### 10. VIX position-size multiplier
**Question:** Should VIX-based size scaling stay mechanical?
**Research:** `positionSizing.js:45-62` — 1.0/0.75/0.50 ladder by VIX level,
correctly implemented. Two refinements found: (a) the multiplier is
frequently a silent no-op — it only bites when the position-cap branch is
the binding constraint, with no on-screen indication when it isn't; (b) the
identical threshold ladder is duplicated verbatim at `App.jsx:359` and
`App.jsx:381` (Code Architecture Rule 7 violation), and both read
`rawAnalysisData?.vix?.current` — opening the calculator without having
analyzed a stock silently defaults to `1.0` (a Day-54 silent-fallback shape).
**Reasoning:** The calculator is opt-in arithmetic the human explicitly
triggers after entering their own account size/risk% — categorically
different from a standing verdict shown unprompted on the main analysis
view. Keeping this one lever mechanical is consistent with "mechanize what
governs a moment humans are bad at" (sizing under a losing streak) — but
only inside the tool the human deliberately opened.
**Decision:** **Engine** inside the calculator; **Info** (a plain VIX
number, no multiplier shown) on the main Trade Setup card.
**Fixes to fold in:** extract the duplicated ladder to one exported
`getVixPositionMultiplier()` in `positionSizing.js`; surface the "VIX
unknown → defaulting to 1.0×" case explicitly instead of silently.
**What this does NOT change:** `calculatePositionSize()`'s core math.
**Status:** Locked.

---

### 11. MTF Confluence, S/R lists, Price Structure, Pattern Detection,
### Breakout Status
**Question:** Do these need redesigning to match the new philosophy?
**Research:** Confirmed `breakout_detection.py:5`'s own docstring: *"It is
intentionally a human-in-the-loop filter, not an auto-trading decision
engine."* These cards already are the target pattern — descriptive states,
confidence percentages, watch-item bullets, never suppressing anything else.
**Reasoning:** Redesigning something that already embodies the target
philosophy would be churn, not improvement.
**Decision:** **Info**, unchanged — these are the reference implementations
everything else in this redesign is modeled on.
**Caveat (Pattern Detection only):** its per-pattern R:R
(`categoricalAssessment.js:61-89`) uses a **fixed target multiple**
(1.12-1.20× pivot), never checked against real resistance — structurally
identical to the already-logged SRPS screener flaw
(`KNOWN_ISSUES_DAY108.md:85-87`). It's correctly info-only, but its number
reads as an earned R:R when it's by-construction. If an honesty caveat is
added to any R:R display on this page (§6), the same one-line note belongs
here too. Low effort, not yet scheduled — see §9.
**Status:** Locked.

---

### 12. Composite verdict → Technical Read + Regime band (Option A)
**Question:** How should the top-of-page verdict be redesigned, given items
4 and 5 above pull it in two different directions (regime should stay a
gate; fundamentals should not)?
**Research:** Two implementation options were spec'd. **Option A** (chosen):
rename to a "Technical Read," driven only by `assessTechnical()` +
(originally) a regime gate — zero change to `determineVerdict()`/
`categorical_engine.py`, zero parity re-verification needed. **Option B**
(not chosen): keep BUY/HOLD/AVOID language, recompute from Technical+Regime
only — requires editing the parity-tested module directly.
**Reasoning:** Option A is the load-bearing reason this work qualifies as
freeze-independent under `ROADMAP.md`'s sole-focus rule — it touches zero
parity-tested code, therefore zero risk to the 86,400-combo test, therefore
zero risk to `live_signals.py`'s import chain. But a single gated badge
(Technical Read gated by regime) is a **category error**: an Unfavorable
regime doesn't make a stock's own technicals weak — SPY below its 200-SMA
says nothing about whether NVDA's Trend Template is 8/8. A badge reading
"Technical Read: Weak" because of VIX would tell the user something false
about the stock itself.
**Decision:** **Engine, narrowed and split into two elements:**
- **Technical Read: Strong/Developing/Weak** — purely `assessTechnical()` +
  the ADX modifier (item 2). Never gated by regime. Honest to its own name.
- **A separate, always-visible Regime band** (item 4) that carries the
  actual gate.
`determineVerdict()`'s code is untouched either way — this is purely a
display-layer decision about which computed value(s) become the headline.
**Orphaned consumers requiring explicit disposition** (found this round,
not in the original plan):
| Consumer | Disposition |
|---|---|
| `App.jsx:1660-1664` "⚠️ Stock not recommended" (AVOID+viable contradiction) | **Delete** — exists only to reconcile two things being removed |
| `App.jsx:1699-1704` position-size-advice suppression condition | **Delete with its whole block** (item 9) |
| `App.jsx:2506-2521` "Why This Verdict?" | **Reframe** to "How this read was formed," neutral container, driven by the new read + regime |
| `App.jsx:2742-2755` Simple view's "Full Assessment (for comparison): BUY" | **Delete** (item 12c below) |
| `App.jsx:3601` `categoricalVerdict` on manually-logged forward-test trades | **Keep unchanged** — a data field for continuity with historical `localStorage` trades, not a display element |
**The cross-tab vocabulary question, resolved:** the Scan tab's on-demand
verdict column and the paper-trading engine keep BUY/HOLD/AVOID language —
this is an **acceptable, honest split**, not sloppiness, because both run
the actual frozen/pre-registered decision engine for a genuinely different
purpose (batch triage; live entry gating). Ratified on one condition: it's
labeled, not silent — add one line under the Scan column header: *"Scan-tab
verdict uses the frozen backtested BUY/HOLD/AVOID tree, the same engine the
paper-trading tracks are pre-registered against. The Analyze page's read is
a separate, display-only summary."*
**What this does NOT change:** `determineVerdict()`'s code, its parity
coverage, or the Scan tab / paper-trading engine's use of it.
**Status:** Locked — split into two elements (resolved via AskUserQuestion,
Recommended option taken).

---

### 12c. Simple Checklist view — vocabulary reconciliation
**Question:** With the Full view renamed to "Technical Read," does the
Simple view's own BUY/HOLD/AVOID comparison strip create a 3rd vocabulary
on the same page?
**Research:** `App.jsx:2742-2755`, labeled "Full Assessment (for
comparison)," re-displays `categoricalResult.verdict.verdict`
(BUY/HOLD/AVOID) directly inside the Simple Checklist view (whose own
verdict is TRADE/PASS). Two vocabularies on the same page, one click apart,
would become three once the Full view says "Technical Read."
**Reasoning:** The strip's only function was cross-checking two verdict
systems being presented as commensurable — once they're not, the comparison
has nothing left to justify it.
**Decision:** **Delete** the comparison strip; keep the "View Full
Analysis →" link in its place.
**What this does NOT change:** The Simple Checklist's own 9-criterion logic
or its TRADE/PASS verdict (see item 14 below).
**Status:** Locked.

---

### 13. Holding Period selector
**Question:** What should it do once Fundamentals no longer drives verdict
weighting?
**Research:** Grep-confirmed: `holdingPeriod` is never read by
`riskRewardCalc.js` or `positionSizing.js` — its only mechanical consumer is
`determineVerdict()` via `getSignalWeight()` (Quick 70/30, Standard 50/50,
Position 30/70, Tech/Fund). **Correction from an earlier pass:**
`getSignalWeight()` is **not retired** — it's still called
(`categoricalAssessment.js:693`), still returned in every result payload,
still exercised by the parity test across all 3 holding periods. What
retires is only its *visible* effect on the page (since the composite
verdict it feeds is no longer the headline).
**Reasoning:** The underlying insight — fundamentals matter more over a
longer hold — is sound, ordinary trading wisdom, not something to discard
just because the mechanism built on it (a scored weight feeding a gate) is
going away.
**Decision:** **Repurposed, still Info** — controls only the visual
prominence of the Fundamentals red-flag card (collapsed/de-emphasized on
Quick, surfaced more prominently on Position). Never gates anything.
**Required copy fix (Layer-1 consistency, or these become false claims):**
`App.jsx:1366` and `:1379` currently display "Tech 50% / Fund 50%"-style
strings that no longer reflect anything visible on the page — replace with
the horizon label only ("Standard Swing — 15-30 days").
**What this does NOT change:** `getSignalWeight()`'s code, its return
value, or its parity coverage — only its consumption for display purposes.
The re-assessment effect (`App.jsx:263-273`) that re-runs on holding-period
change is also **kept**, since `determineVerdict()`'s output still feeds
the retained `categoricalVerdict` trade field (item 12) and the reframed
"how this read was formed" panel.
**Status:** Locked.

---

### 14. Default view (Full Analysis vs. Simple Checklist)
**Question:** The page the user actually lands on (`App.jsx:148`, default
`'simple'`) is untouched by all 13 decisions above, and is more prescriptive
than anything being redesigned (a `text-4xl` "✅ TRADE / ⏸️ PASS," "ALL 9
criteria must be YES... No exceptions," a hard R:R≥2.0 gate, a hard ADX≥20
gate). Should the default change?
**Research:** `App.jsx:2603` onward is the Simple view. Its methodology
note is at `:2735-2737`. Its own already-logged, unresolved Known Issue:
*"Simple Checklist's 'PASS' badge is misleading at low pass counts... no
decision made on rewording yet"* (`KNOWN_ISSUES_DAY108.md:81-83`).
**Reasoning:** Without this change, the redesign's philosophy shift lives
entirely behind a click the user has to remember to make — the page they
see first stays exactly as mechanical as before.
**Decision:** **Change the default to `'full'`** (`App.jsx:148`). Simple
Checklist remains fully available, completely unchanged in logic, as an
explicit opt-in mechanical instrument for anyone who wants pure pass/fail —
it is a deliberately mechanical tool (backtest-anchored to Config C) and
redesigning its logic would be a Golden Rule 18/20 threshold re-tune, out of
scope entirely.
**Bonus, zero-cost while touching this view:** the "PASS badge misleading"
Known Issue can close in the same session as pure copy —
`0/9 criteria met — No Trade` instead of a bare "PASS" — zero logic change.
**What this does NOT change:** `simplifiedScoring.js`'s 9 criteria, their
thresholds, or the TRADE/PASS verdict logic itself.
**Status:** Locked (resolved via AskUserQuestion, Recommended option taken).

---

## §3 — Corrections to earlier passes

Recorded explicitly so the doc stays trustworthy — per Golden Rule 6 and
`PERSONA.md`'s "don't invent a finding to justify the ritual" (Golden Rule
41's carve-out also cuts the other way: don't let a wrong finding survive
either).

1. **`generateActionableRecommendation()` was claimed as a removed
   imperative banner ("READY TO TRADE"/"SKIP THIS ONE"), credited to the
   redesign's philosophy shift.** It is dead code — defined at
   `App.jsx:880-1028`, called from nowhere (`grep -rn
   "generateActionableRecommendation" frontend/src/` returns exactly one
   hit, the definition itself). It renders nothing today. Still worth
   deleting, but as ordinary dead-code cleanup (the Day-53 "255 unused
   lines" pattern), not as a UX change this redesign should take credit for.
2. **The original reasoning for item 7 (R:R) cited "3 different R:R
   minimums scattered across the app with no single threshold" as the
   problem.** That finding was already investigated and explicitly closed
   as *not a bug* in `KNOWN_ISSUES_DAY108.md:8` ("three genuinely different
   UI surfaces, three different purposes — no inconsistency... Closing").
   Re-asserting it would have put a closed non-finding back into a
   permanent document. Replaced with the real, verified problem: 4 different
   R:R *formulas* (§4), two of which print on the same card under the same
   label while measuring different things.
3. **Item 13's original wording said Holding Period's verdict-weighting
   purpose was "retired."** `getSignalWeight()` is still called, still
   returned in every payload, still exercised across all 3 holding periods
   by the parity test. Only its *visible* influence on the page retires —
   the function and its behavior do not change. A future session reading
   "retired" and deleting the function would have broken parity on 28,800
   of the 86,400 test combos.
4. **Item 5's original wording said Fundamentals become "fully excluded
   from `determineVerdict()`'s counted `strongCount`."** Under Option A
   (item 12), `determineVerdict()` is not modified — Fundamentals remain in
   the internal `strongCount` calculation. What changes is that the
   composite output is no longer displayed. See item 5's full entry above
   for the corrected framing.

---

## §4 — The R:R landscape

Four different quantities are all called "R:R" somewhere in this app. None
of them are wrong for their own purpose; the problem is that two of them
(#1/#2 and #3) appear on the same card, one paragraph apart, under
overlapping labels, with nothing on screen explaining they answer different
questions.

| # | Formula | Where computed | Where displayed | Purpose |
|---|---|---|---|---|
| 1 | `(target − support) / (2×ATR)` | `riskRewardCalc.js:30-33` | `App.jsx:1880-1882` ("R:R") | Pullback entry-strategy panel |
| 2 | `(target − price) / (price − (support − 1.5×ATR))` | `riskRewardCalc.js:36-39` | `App.jsx:1933-1935` ("R:R") | Momentum entry-strategy panel |
| 3 | `resistance_dist_pct / support_dist_pct` — a ratio of *percentage distances*, no ATR, no stop | `support_resistance.py:475-480` | `App.jsx:1712` ("R:R Context") | Backend advice banner, sits directly above panels 1/2 |
| 4 | `(nearest_resistance − price) / (price − nearest_support)` | `live_signals.py:176-181` | Not displayed — live gate only, `MIN_RR 1.2` | Path B automated entry gate |

Both real, still-open bugs upstream of every row above:
- **Pivot S&R selects the most extreme level in range, not the nearest
  one** — `support_resistance.py:1049-1051` (`highs[-5:]` / `lows[:5]` on a
  price-sorted list, before proximity filtering). Confirmed the primary
  method, open Medium severity (`KNOWN_ISSUES_DAY108.md:32-37`). Every row
  above is built on levels selected this way.
- **Golden Rule 35** — the live automated R:R gate (row 4) went from Day 81
  to Day 95 without actually matching the logic `backtest_holistic.py`'s
  Config C used to validate the system, a genuine live/backtest divergence
  that took a targeted investigation to surface.

This table is the "one place" `KNOWN_ISSUES_DAY108.md:8` asked the R:R
documentation to live, taken further than that entry reached.

---

## §5 — The Fundamentals red-flag screen

**Governing principle** (Core Principle 6 — every rule survives "why" three
times; this is the third why for each threshold below):

> A red flag must be robust to the measured disagreement between the two
> data methods. Reuse the scoring band where the metric's sign is stable
> across sources; move the trigger outward where the measured noise lives;
> and where the band encodes quality rather than fact, replace it with a
> factual trigger.

| Metric | Current scoring band (`categoricalAssessment.js`) | **Red-flag trigger** | Reasoning |
|---|---|---|---|
| Revenue Growth | Weak = `< 0%` (`:395-398`) | **≤ −10% YoY** | The 0% line sits exactly where a TTM-vs-annualized-quarterly method difference flips sign — this is the measured *dominant driver* of the 40% mismatch (`KNOWN_ISSUES_DAY92.md:53`). −10% is far enough outside the disagreement envelope that both data methods agree it's a genuine decline. Moved outward deliberately, not arbitrarily. |
| Debt/Equity | Weak = `> 2.0` (`:408-411`) | **> 2.0 — unchanged** | A point-in-time balance-sheet ratio, minimally affected by TTM-vs-quarterly windowing. Also the one threshold here that already survived independent scrutiny once (`VALUE_TAB_SPEC.md` §2 explicitly rejected the folklore D/E<0.5 while keeping a leverage concept at a similar order of magnitude). Band reused as-is. |
| ROE | Weak = `< 8%` (`:383-385`) | **< 0% (negative)** | `<8%` is a *quality* judgment — a fine scoring input, but a red flag should be a *fact*. "ROE 7.2%" is a mediocre business, not a warning. Negative ROE (the company lost money on equity) is sign-stable across data sources and a genuine fact. |
| Negative EPS | Not assessed today | **OPEN — needs a data-shape check first** | `epsGrowth` is fetched and stored but never used in any assessment. Whether it represents a growth rate or an earnings level determines whether it can safely carry an "unprofitable" flag. Not specified until verified against a live payload (Golden Rule 3 — never assume structure). See §9. |

**Three non-negotiable display rules** (all Golden Rule 44 / Day-54
applications):
1. **Three distinct states, never collapsed to two:** "No red flags found"
   ≠ "Screen unavailable — fundamentals data not returned" ≠ "N flags."
   `assessFundamental()` already distinguishes `'Unknown'` from a real
   assessment (`:350`, `:417`) — the display must not flatten these into a
   falsely reassuring "no flags."
2. **ETFs get "Not applicable — ETF,"** reusing the existing `isETF` branch
   (`:337-345`), never "no flags."
3. **One permanent honesty line on the card**: the underlying bands were
   validated as *scoring inputs* against SimFin data, not as a red-flag
   screen against live TTM data — the screen itself is unvalidated, and the
   card says so (exact copy in §6). Same discipline as the HUB-65
   selection-bias caveat (`PERSONA.md` Day-98 entry: state it loudly and
   everywhere the number appears, not quietly once).

---

## §6 — Final copy

Every technical block below now carries a paired **Plain-English line** —
shown directly underneath the technical copy, muted/smaller, same visual
convention as the honesty notes this section already used (Golden Rule-style
"translate the jargon, don't just gate on it"). Added Day 111, in response to
a direct request that every card's technical label ship with a
non-technical-reader translation alongside it, not instead of it.

**Page subtitle** (under the ticker):
> Independent reads, shown side by side. You make the call.

**Regime band** (Day 111: rewritten to match the Day 110 reversal — Info,
not a gate; no imperative "stand-down" language; kept expanded by default
since regime is portfolio-wide, not single-stock — **this also closes the
mockup-sync gap tracked in §9/`KNOWN_ISSUES_DAY110.md`, the copy below is
now the single source of truth**):

> 🟢 **Regime: Favorable** — VIX 16.4, SPY above its 200-day SMA.
> Plain-English: *The overall market backdrop is calm and healthy —
> generally a good environment for new trades.*
>
> 🟡 **Regime: Neutral** — VIX 24.1 (elevated), SPY above its 200-day SMA.
> Plain-English: *The market's a bit jumpy right now. A good setup is still
> a good setup, just maybe size it smaller.*
>
> 🔴 **Regime: Unfavorable** — SPY below its 200-day SMA.
> Plain-English: *The broader market is in a downtrend. Even a great-looking
> stock is swimming against the tide — worth weighing before you commit
> capital.*

**Technical Read chip:**
> **Technical Read: Strong** · Trend Template 8/8, RSI 65.9, RS 1.03
> Plain-English: *This stock is in a healthy uptrend and beating the
> market — the classic "leader" pattern.*
>
> **Technical Read: Strong · trend not yet confirmed (ADX 14.2)** ← ADX<20
> modifier
> Plain-English: *The setup checks out on paper, but the move hasn't shown
> real conviction yet — could still take off, could also fizzle. Worth a
> tighter entry or a little patience.*
>
> **Technical Read: Developing**
> Plain-English: *Some of the uptrend boxes are checked, not all — this
> could turn into a leader, but it isn't one yet.*
>
> **Technical Read: Weak**
> Plain-English: *This doesn't look like a market leader right now — either
> the trend or the relative performance is lagging.*
>
> **Technical Read: Unavailable** — pattern detection didn't return for
> this ticker
> Plain-English: *We couldn't run the trend read for this ticker — try
> again in a moment.*

**Sentiment card** (Fear &amp; Greed — no copy previously drafted for this
section; added Day 111 to close that gap):
> **Sentiment: Neutral (F&amp;G 47)**
> Plain-English: *Investors aren't especially fearful or greedy right now —
> no crowd extreme to lean against.*
>
> **Sentiment: Extreme Fear (F&amp;G 14)**
> Plain-English: *The crowd is panicking. Historically that's sometimes a
> good time to buy, not a reason to run.*
>
> **Sentiment: Extreme Greed (F&amp;G 88)**
> Plain-English: *The crowd is euphoric. Historically that's when pullbacks
> tend to start — a caution flag, not a sell signal.*
>
> **Sentiment: Unavailable**
> Plain-English: *We couldn't pull sentiment data right now.*

**R:R below-1.0 note** (muted, teal-bulleted, same grammar as Price
Structure's watch items):
> • R:R is 0.34 because the nearest resistance (R1 $227.49) is only 1.0%
> above price while the ATR-based stop sits 7.1% below. The constraint is
> target proximity, not stop placement.
> Plain-English: *For every $1 you're risking, this setup only offers about
> 34 cents of reward to the nearest resistance — not great odds, at least
> to that first target.*
>
> • *(Shown only when `srData.meta.resistanceProjected` is true.)* This
> stock is at or near its all-time high, so there's no real overhead
> resistance to aim at. The target in this ratio is a projected level
> (ATR/Fibonacci), not a price where sellers have actually shown up before.
> Read the number as one input, not a verdict.
> Plain-English: *There's no "ceiling" on the chart above this price yet,
> so the target is an estimate — treat the reward side of this ratio as a
> guess.*
>
> *(Day 121 correction, Phase 0 of the Day 119 plan — Correction C1: the
> bullet previously here said the S&R levels came from a pivot method that
> picks the most price-extreme levels rather than the nearest. That was
> fixed Day 112 — `support_resistance.py` `pivot_nearest_selection = True`,
> re-checked Day 121 — so the old bullet would have described a bug that no
> longer exists. The honest caveat today is the projected-target case
> above: `calculateRiskReward()`'s reward leg is `srData.suggestedTarget`,
> which is a synthetic projection whenever `resistanceProjected` is true,
> and nothing on the live card says so.)*

**R:R footnote** (persistent, replaces any "3 thresholds" framing — see §3
correction 2):
> **Note on the R:R numbers on this page.** Several numbers here are
> labeled R:R, and they measure different things, so they won't match. The
> two entry panels both aim at the same target (the nearest resistance) but
> use different entries and stops: pullback enters at support with a stop
> 2×ATR below it; momentum enters at today's price with a stop 1.5×ATR below
> support. "R:R Context" in the setup banner is just distance-to-resistance
> divided by distance-to-support, in percent — no stop, no ATR. The Pattern
> Detection card measures from the pattern's own pivot, with a stop 2×ATR
> below the pivot and a target from the pattern's measured move (or, for a
> VCP, the nearest real resistance). All are shown; none gates anything.
> Plain-English: *You'll see a few different "R:R" numbers here — they're
> calculated differently and answer slightly different questions. They're
> not supposed to match each other.*
>
> *(Day 121 correction, Phase 0 — Correction C2: the footnote previously
> said the Pattern Detection card's R:R used a fixed 1.12-1.20× pivot
> multiple, not real resistance. That formula was replaced Day 112
> (measured-move target, `categoricalAssessment.js` `measuredMoveTarget()`)
> and Day 118 (VCP: nearest real resistance, `vcpTarget()`), and the card
> now returns no R:R at all rather than inventing one when there's no
> target. Pattern Detection stays in the footnote — its R:R is still
> computed differently from the entry panels' — but it's no longer on the
> "not real resistance" list. Stop formulas re-checked against
> `riskRewardCalc.js:30,36` and `categoricalAssessment.js:142` on Day 121.)*

**Sizing inputs grid** (header + framing):
> **Sizing inputs** — the raw numbers, no recommendation. Position sizing is
> roughly 90% of a system's results (Van Tharp); it's the last thing this
> page will decide for you.
> Plain-English: *We're giving you the ingredients, not the recipe — how
> much to buy is your call.*
>
> [ADX] [ATR] [Stop distance — pullback] [Stop distance — momentum] [RVOL]
> [VIX]
>
> Plain-English per stat: ADX — *how strongly this stock is currently
> trending.* ATR — *how much this stock typically moves in a day; a bigger
> number usually means a wider stop.* Stop distance % — *how far below your
> entry the stop-loss would sit.* RVOL — *is today busier or quieter than
> usual? Below 1.0 means quieter.* VIX — *a gauge of how nervous the overall
> market is right now.*
>
> ADX below 20 means no confirmed trend. A wider stop means fewer shares for
> the same dollar risk. RVOL below 1.0 means today's volume is lighter than
> the 50-day average.
>
> [ Size the pullback entry → ]  [ Size the momentum entry → ]

Both CTAs are unconditional — no viability gate — and reuse the existing
purple button style and `autoFillPositionCalculator()`.

**Fundamentals red-flag card** (four states):
> **Fundamentals — context, not part of the read**
>
> No red flags found. *(ROE 31.2% · Revenue growth +8.4% · Debt/Equity
> 0.41)*
> Plain-English: *The underlying business looks healthy — profitable,
> growing, and not overloaded with debt.*
>
> ⚑ **1 red flag** — Revenue declining −12.4% YoY.
> Plain-English: *Sales are shrinking. Worth understanding why before
> holding this for weeks or months.*
>
> Screen unavailable — fundamentals data didn't return for this ticker.
> Plain-English: *We don't have financial data for this stock right now —
> can't tell you either way.*
>
> Not applicable — ETF.
> Plain-English: *This is a fund, not a company — there's no balance sheet
> to check.*
>
> ⓘ *This screen flags facts, it doesn't score. The live fundamentals feed
> disagrees with the data this system was backtested on about 40% of the
> time (measured on 20 liquid tickers; revenue growth is the biggest
> driver), which is why it informs rather than gates. Flag thresholds are
> chosen to sit outside that measured disagreement — they have not
> themselves been backtested.*

**Holding-period selector header** (replaces the "Tech 50%/Fund 50%"
string):
> Holding Period · Standard Swing (15-30 days)
>
> *Sets how prominently the fundamentals screen is shown — longer holds
> surface it, shorter holds collapse it. It doesn't change any read.*
> Plain-English: *How long you plan to hold changes how much the
> Fundamentals section matters — over months, a company's health counts for
> more than it does over days.*

**Scan tab disclosure line** (one line under the "STA Verdict" column
header, per item 12's cross-tab resolution):
> Scan-tab verdict uses the backtested BUY/HOLD/AVOID tree, unchanged so it
> stays comparable with the backtest results. The Analyze page's read is a
> separate, display-only summary.
>
> *(Day 121 correction, found during Phase 0, not in the Day 119 plan: the
> old line said the tree was the engine "the paper-trading tracks are
> pre-registered against." The paper-trading program was discontinued Day
> 113, so that reason no longer holds. The tree is still kept unchanged, now
> for backtest/parity comparability — the same grounds the Day 119 plan's
> §D gives for leaving the backend alone.)*

---

## §7 — Implementation plan

> **Superseded for execution (Day 119):** build from
> `docs/claude/design/ANALYZE_PAGE_REDESIGN_IMPLEMENTATION_PLAN_DAY119.md`
> §E, not from §7/§8 below. Its line anchors have drifted and §8's freeze
> rationale no longer applies (paper trading discontinued Day 113). §7/§8
> are kept as the historical record.

Not executed this session — recorded for when the user asks for it.

### §7.0 — Freeze safety audit (do this first if implementation ever starts)

| File | Touched? | Why |
|---|---|---|
| `backend/support_resistance.py` | **NO** | Feeds live Path B (`live_signals.py:167-191`). Absolutely frozen. |
| `backend/backtest/categorical_engine.py` | **NO** | Parity contract; imported by `live_signals.py:47`. |
| `backend/paper_trading/*` | **NO** | The 4 live tracks. |
| `backend/backend.py` | **NO** | `/api/sr/<ticker>` response shape unchanged; frontend just ignores 2 fields. |
| `frontend/src/utils/categoricalAssessment.js` | **ADD ONLY** | The 5 parity-exported functions stay byte-identical; new display helpers appended after line 914. |
| `frontend/src/utils/riskRewardCalc.js` | Yes | Delete `getViabilityBadge()` (`:86-95`), `hasViabilityContradiction()` (`:71-78`). `calculateRiskReward()` unchanged. |
| `frontend/src/utils/positionSizing.js` | Yes (small) | Add exported `getVixPositionMultiplier()`; core calculator unchanged. |
| `frontend/src/App.jsx` | Yes (bulk) | Display layer only. |
| `frontend/scripts/ui-verify-checklist.js`, `ui-cohesiveness-test.js` | Yes | Currently assert the OLD behavior as pass conditions — must update in the same commit or they falsely certify the pre-redesign UI. |
| `frontend/scripts/verdict_grid.mjs` | **NO** | Its imports must keep resolving — proof parity is untouched. |
| `backend/backtest/test_verdict_parity.py` | **NO** | Run it; don't edit it. |

### §7.1 — Phase 1: additive utilities (no visible change, independently
verifiable)
`categoricalAssessment.js` — append after line 914: `deriveTechnicalRead()`,
`screenFundamentalRedFlags()`, `describeRegimeGate()`. None call
`assessFundamental()`/`assessTechnical()` internals in a way that risks
parity — they consume already-computed outputs. `positionSizing.js` — add
`getVixPositionMultiplier()`.
**Verifiable now:** `test_verdict_parity.py` still passes untouched (nothing
above line 914 moved).

### §7.2 — Phase 2: Trade Setup card
Remove the viability badge, gate/suppression classes, `Position` rows
(fixes the hardcoded "half"), "R:R Context" display; add Risk/Reward-per-
share rows, the below-1.0 note, the R:R footnote, and the shared Sizing
Inputs grid with its two CTAs.
**Verifiable now:** both entry panels render at full opacity for a
known-bad-R:R ticker; `grep -r "position_size_advice" frontend/` returns
zero.

### §7.3 — Phase 3: top-of-page (Technical Read + Regime band)
Replace the composite verdict pill with the two-element split; add the
subtitle, the uniform reads strip, and the regime band; rewrite the
holding-period selector's collapsed label; delete
`generateActionableRecommendation()` (dead-code cleanup, not a UX claim);
demote the Fundamentals-unavailable banner into the new Context card.

### §7.4 — Phase 4: Fundamentals context card + Assessment Breakdown
New "Context — not part of the read" card (red-flag screen + Sentiment,
prominence driven by holding period); Fundamental tile gains
`infoLabel="(info)"` + `opacityMuted` matching Sentiment's existing
treatment; "Why This Verdict?" reframed to "How this read was formed."

### §7.5 — Phase 5: Simple-view reconciliation
Delete the "Full Assessment (for comparison)" strip; change the default
view to `'full'` (`App.jsx:148`); fold in the "PASS badge" copy fix
(`0/9 criteria met — No Trade`) as a zero-risk bonus.

### §7.6 — Phase 6: tests + docs (same commit as Phases 2-5, non-negotiable)
Update `ui-verify-checklist.js` and `ui-cohesiveness-test.js`'s assertions
to match the new DOM; update `HOW_STOCK_PICKING_WORKS.html`, `README.md`,
`DEVELOPER_ONBOARDING.md`; add a `ROADMAP.md` priority entry categorizing
this as freeze-independent display work; append a change-log entry here
(§10).

### §7.7 — Sequencing
Phase 1 lands first (Phases 2-4 consume its helpers). Phases 2/3/4 are
independent of each other. Phase 5 depends on Phase 3 for vocabulary
consistency. Phase 6 ships in the same commit as 2-5, always.

---

## §8 — Freeze safety audit

See §7.0 for the file-by-file table — reproduced there because it's also
the first thing an implementation session needs to check, not just a
verification afterthought.

**The two disclosures that make this claim honest, not just asserted:**
- Fundamentals will keep gating real, live momentum-track entries via
  `categorical_engine.py`/`live_signals.py` even after the Analyze page
  stops presenting Fundamentals as a gate to the human. Intentional
  (changing it would reset a live track's trade count), disclosed here per
  constraint 3 in §1.
- `support_resistance.py`'s `position_size_advice`/`risk_reward_context`
  fields keep being computed and returned by the backend unchanged — only
  the frontend stops reading them. Nothing server-side changes.

---

## §9 — Open items

| Item | What would close it | Why it's open |
|---|---|---|
| ~~Negative-EPS red flag~~ — **CLOSED: checked, declined (Day 119, recorded Day 121)** | Done | `epsGrowth` is a YoY growth *rate*, not an earnings level (`providers/base.py:31`; `yfinance_provider.py:166` computes `(current − year_ago) / abs(year_ago) × 100`). A negative value means earnings fell, not that the company loses money, and the `abs()` denominator makes the sign misleading when the prior year was a loss. Red-flag screen ships with §5's three metrics only (revenue ≤ −10%, D/E > 2.0, ROE < 0). See Day 119 plan, Correction C4. |
| ~~Pattern Detection card's fixed-multiple R:R caveat~~ — **CLOSED by Days 112/118 (recorded Day 121)** | Done | The fixed multiple no longer exists: measured-move targets (Day 112) and VCP nearest-resistance targets (Day 118) replaced it. §6's footnote rewritten to match. See Day 119 plan, Corrections C2/C3. |
| `/api/sr/<ticker>`'s duplicate backend/frontend R:R arithmetic (item 8) | Post-freeze DRY cleanup | Touches `backend.py`'s S&R route, upstream of `compute_sr_levels` — deferred, not urgent |
| No visual mockup built yet | Build the Artifact once remaining copy/threshold questions are closed | User explicitly asked for decisions to finalize before the mockup, not in parallel |
| ROADMAP.md priority entry for this work | Add during §7.6 (docs phase) if/when implementation starts | Not yet added — this design doc exists independently of the roadmap today |
| `scoringEngine.js`'s orphaned fundamentals score (incl. Forward P/E) — dead but not deleted | Delete `generateScoreExplanation()` (`App.jsx:1032-1071`) and `getSubScoreInfo()` (`App.jsx:1074-1091`) in the same pass as item 3's other dead-code cleanup, or explicitly wire them up if ever needed | Traced Day 111: `calculateScore()` itself is live (`App.jsx:448/651`, its `.breakdown.technical` feeds `runCategoricalAssessment()` directly) but its **fundamental** point-score — 5 metrics incl. Forward P/E, different thresholds than `assessFundamental()` for the same 3 shared metrics (e.g. ROE weak-line 8% vs. 10%, Debt/Equity strong-line 1.0 vs. 0.5) — is computed every run and stored in `analysisResult.scores.fundamental`/`analysisResult.details`, but the only two functions that would ever render it are defined and never called anywhere in the file (confirmed via grep, zero invocations). Not a live conflict today; a landmine if either function is ever wired up without this context — it would silently reintroduce a 3rd, differently-thresholded fundamentals verdict next to the redesigned red-flag card. |
| Item 16 (new, Day 111-112): Volume Confirmation — **SHIPPED on the live page** | Done | ROADMAP Priority #11's volume-confirmation gap redesigned to match this doc's own Info-not-gate philosophy, then actually built — but not on "the Technical Read card" as originally planned. A dedicated Opus pass found Technical Read and the Sizing Inputs grid only exist in this doc's own unimplemented mockup; the live page has neither yet. Shipped instead on the live Trade Setup card (`App.jsx`, ~line 1808+), reusing the live RVOL computation and a newly-deduplicated 1.5x threshold (`frontend/src/utils/volumeThresholds.js` — the "already shared" threshold turned out to be 7 unlinked copies, now fixed on the frontend side). **Day 112 extension, also shipped:** a second line answering "buying or selling," combining day's price change, close-location-in-range (new `meta.candle` backend field), and OBV trend into an honest lean — "leans toward buying pressure" / "…selling pressure" / "mixed signals, no clear lean" / "no clear lean either way," explicitly never a verdict, since daily bars can't show real order flow. A second Opus pass found a real, pre-existing OBV sign bug along the way (logged in `KNOWN_ISSUES_DAY110.md`, not fixed — out of scope for a display-only change). **Re-homing note for whenever this redesign actually ships:** this note belongs on Technical Read once that card exists; until then it lives on Trade Setup so it isn't waiting on the whole redesign to land. Companion item (Dual/Absolute Momentum) decided **not** to pursue — tested clean but near-inert, correct but not worth the complexity. |

---

## §10 — Change log

- **Day 109:** Document created. 13 items locked via iterative Q&A
  (user-driven), validated and corrected by a dedicated Opus review pass (4
  corrections, 4 additional decisions resolved: default view, ADX modifier,
  Technical Read/Regime split, evidence-based red-flag thresholds). Full
  implementation plan drafted, not executed. No application code changed.
- **Day 111:** §6 rewritten — every card's technical copy now carries a
  paired plain-English line (Regime, Technical Read, Sentiment, R:R, Sizing
  Inputs, Fundamentals, Holding Period), plus a new Sentiment card copy block
  that didn't exist before. Regime band copy replaced with the actual Day 110
  post-reversal wording (Info-toned, no "stand-down" language) — this is now
  the single source of truth; the published mockup `.html` file itself still
  needs a separate update to match, tracked in `KNOWN_ISSUES_DAY110.md`. New
  §9 open item: `scoringEngine.js`'s orphaned fundamentals score (incl.
  Forward P/E) is dead-but-not-deleted — traced directly, confirmed a landmine
  not a live conflict. No application code changed.
- **Day 119:** Execution plan superseded by
  `ANALYZE_PAGE_REDESIGN_IMPLEMENTATION_PLAN_DAY119.md` (9 corrections; the
  17 decisions unchanged). This file was not edited that day.
- **Day 121 — Phase 0 of the Day 119 plan.** §6 copy corrected: the R:R
  below-1.0 note's second bullet (C1 — the pivot extreme-vs-nearest bug, fixed
  Day 112, replaced with a `meta.resistanceProjected` caveat) and the R:R
  footnote (C2 — Pattern Detection no longer uses a fixed multiple; footnote
  now describes each R:R accurately, stop formulas re-checked against code).
  Also corrected, not in the Day 119 plan: the Scan-tab disclosure line still
  cited "the paper-trading tracks" as the reason the tree is frozen
  (discontinued Day 113). §9: negative-EPS (C4) and Pattern Detection caveat
  (C3) recorded as closed. Pointer to the Day 119 plan added at §7.
  **Baseline captured (Day 121, before any app code changes):**
  - `backend/backtest/test_verdict_parity.py`: **PASS**, 86,400/86,400
    combinations match (technical/fundamental/risk_macro/verdict all 0
    mismatches).
  - `frontend/scripts/ui-verify-checklist.js AAPL`: **FAILS (pre-existing)** —
    "Waiting failed: 60000ms exceeded" at the results-loaded wait, as §B7 of
    the Day 119 plan predicted (waits for "Holding Period", which only renders
    in Full Analysis; default view is Simple).
  - `frontend/scripts/ui-cohesiveness-test.js AAPL`: **FAILS (pre-existing)** —
    same 60s timeout, same cause.
  - These two failures predate the redesign; they are not regressions. Phase
    5's default flip is expected to fix their entry point.
  - **Side effect, logged for Phase 6:** `ui-verify-checklist.js:702`
    hard-codes its output to
    `docs/test/UI_Cohesiveness_Test_Day53_AllPeriods/VERIFICATION_REPORT.md`,
    and that folder is untracked in git. Running the baseline overwrote the
    Day 53 report with today's failure report; the Day 53 content isn't
    recoverable from git, and no summary of it exists in the status
    archives. The PDFs in that folder are untouched. Phase 6 should write to
    a dated folder instead. No application code changed.
- **Day 121 — Phase 1 (helper functions), user sign-off:** 3 functions added
  to `categoricalAssessment.js` (`deriveTechnicalRead`,
  `screenFundamentalRedFlags`, `describeRegimeRead`) and 1 to
  `positionSizing.js` (`getVixPositionMultiplier`). Pure additions, not yet
  imported; parity still 86,400/86,400. **User approved (Day 122):**
  - The Engine/Info split as built (Technical Read = Engine; Regime,
    Fundamentals, R:R, sizing = Info).
  - The Regime read, including the 3 plain-English lines Phase 1 added for
    cases §6 didn't cover: VIX > 30 with SPY above its 200-day ("very
    nervous… big swings in either direction"); VIX unavailable ("couldn't
    check how nervous it is right now"); 50-day slipping while calm ("an
    early warning sign, not a downtrend"). These are now part of the
    approved copy alongside §6.
- **Day 122 — Technical Read card: 4 key checks (SMA) + 1 timing line (EMA),
  user-approved.** Display change only; the engine still scores all 8
  Trend Template checks, so `determineVerdict()` and the parity test are
  untouched.
  - **Rule:** SMA is for trend ("is this stock in an uptrend?"); EMA is for
    timing ("is now a good moment to get in?"); stops use ATR, neither.
  - **The 4 key checks shown** (all SMA, from
    `pattern_detection.py` `check_trend_template()`): price above the
    200-day; 200-day rising vs 1 month ago; price above the 50-day; price
    within 25% of the 52-week high.
  - **Why these 4:** cross-checked against the 9 canon principles
    (`TRADING_PRINCIPLES_100YR_RESEARCH.md`), the 10-comment Reddit set on
    the principles artifact, and a Day 122 Reddit SMA/EMA research pass
    (user-run, AI-summarised, threads not independently verified). The
    200-day SMA is the only rule all three back. Reddit names the 50 and
    200 as "the most important"; the 150-day is rarely used. Checks #2,
    #4, #5 (the 150-day checks) are Minervini-only, backed by neither
    source; #7 (30% above the 52-week low) mostly repeats #8.
  - **Timing line (Info, never gates):** price vs the 21-day EMA, labelled
    trader practice, not canon (the canon is silent on EMAs). Reddit's most
    common entry reference. Already computed client-side
    (`technicalIndicators.js:136`).
  - **SMA, not EMA, for the 4 checks:** canon (Faber's 10-month SMA) and the
    backtest both use SMA; Reddit itself says the SMA/EMA difference is
    negligible at 50/200 lengths.
  - **Honesty requirement:** because the Read label (Strong/Developing/Weak)
    is still computed from all 8 checks + RSI + RS, the card must also show
    the full engine score (e.g. "Trend Template 8/8") so a 4/4 stock that
    reads "Developing" isn't a visible contradiction.
  - **Later, separate project (not this redesign):** backtest a 4-check
    engine vs the current 8, prediction written down first (Golden Rule
    56). Switch the engine only if 4 does as well or better. This would
    retire the last Minervini-only piece of STA's verdict.

- **Day 122 — "Close to its 1-year high" check kept, 25% cutoff kept
  (user-approved).**
  - **Kept:** strongest canon backing of the 4 (O'Neil's "N", Minervini,
    Darvas/Livermore; George & Hwang 2004 52-week-high study). Partly
    redundant with the 200-day checks, but cheap to show.
  - **Reddit check (Day 122, user-run, AI-summarised, quotes not
    verified):** agrees on the idea (near the high beats far below it;
    "falling knives"). No shared cutoff: some use 5%, many use none.
    Dissent came mostly from long-term value investors. Backtest evidence
    thin (one unsourced 58% hit-rate claim).
  - **Why 25% stays:** it is the engine's number (display must match the
    engine; no engine change in this redesign). A tight cutoff like 5%
    would reject the pullback setups MR (the one confirmed edge) buys.
    No alternative has evidence behind it. Any cutoff change belongs to
    the later 4-vs-8 engine backtest, prediction written down first.

- **Day 122 — Technical Read wording + RSI fallback (user-approved).**
  - Low-ADX modifier reads "taking a breather: moving sideways for now
    (ADX n)", replacing the §6 wording "trend not yet confirmed".
  - When RSI is missing, show "momentum n/a" instead of the silent `|| 50`
    fallback (`categoricalAssessment.js` assessTechnical). Display change
    in the deriveTechnicalRead helper; engine scoring untouched.

- **Day 122 — Timing and volume lines answer their questions
  (user-approved, mockup v0.7).**
  - "Is now a good moment to get in?" gives one of three answers: Yes,
    close to support / Not yet, it's stretched / Not yet, it's below
    support. Canon: don't chase, buy near where you'd be proven wrong
    (Livermore pivotal points, O'Neil "extended", Minervini low-risk
    entry). Reference line stays the 21-day EMA; distance measured in ATR.
    Cutoffs are rules of thumb, untested, and the card says so.
  - Volume moved to its own question, "Are buyers behind the move?":
    Yes / Mixed / No, heavy selling. Canon: Wyckoff and O'Neil (heavy
    volume on up days, light on pullbacks). Replaces the vague "plenty of
    buyers and sellers" line.
  - Both Info only; neither changes the read. Fits MR: points toward
    pullback entries, not chasing.

- **Day 122 — Trend checks 5–8 stay in the engine (user-approved,
  option 1).** User declined a 4-vs-8 backtest; asked whether checks 5–8
  could be archived. Answer: not frontend-only. The 7-of-8 rule lives in
  4 places (`categoricalAssessment.js:342` verdict,
  `pattern_detection.py:282` Stage 2 badge shown on the Analyze page,
  `backtest/categorical_engine.py:71`, `backtest/parameter_stability.py:183`).
  Changing one would let the verdict and the Stage 2 badge disagree on the
  same screen and detach the quoted backtest numbers from the live rule.
  Decision: engine keeps all 8; the card shows 4 plus the full-score line.
  This supersedes the "later 4-vs-8 engine backtest" note above (not
  planned). If 5–8 are ever archived, all 4 places change in one step.

- **Day 122 — Architect-lens fixes to the timing block (user-approved,
  mockup v0.8).**
  - "Support" is reserved for the Trade Setup card's real S&R levels. The
    timing answer now says "close to its 21-day average" / "stretched above
    it" / "below it", so one page never uses "support" for two things.
  - When the read isn't Strong or Decent, the timing answer shows "Not
    applicable: not in an uptrend", so a Weak read can't sit next to "Yes,
    good moment to get in".
  - "Info only, doesn't change the read" stated once above both questions.
  - Full-score line reads "passes 8 of 8 trend checks (the 4 above plus 4
    more)".

- **Day 123 — Technical Read visuals (mockup v0.9, pending user sign-off).**
  - Full-score line became three tiles under "Strong needs all three", each
    with ✓/✗ and its bar: trend 7+ of 8, momentum (RSI) 50–70, beat the
    S&P 500 over the past year. Matches `categoricalAssessment.js:342`.
  - Timing and volume became an "Entry checks" block (Info only): a strip
    showing distance from the 21-day EMA in ATR (close ≤1 ATR, extended
    1–2 ATR still answers Yes, stretched >2 ATR = Keltner Channel default
    band; cutoffs untested), and 20-day volume bars plus the 3 engine votes
    (day change, close location, OBV). Explanations moved behind "why? ⓘ".
  - Data check (Day 123): Tradier, TwelveData and yfinance daily closes
    identical, volume within 0.6% (5 US large caps × 12 days).

- **Day 123 — Momentum rule: logged for one test after the redesign
  (user-decided).** Trader consensus (Brown/Cardwell RSI ranges; "don't
  fade overbought leaders") uses RSI as a floor, not a cap. The 70 cap can
  mark a breaking-out leader Decent instead of Strong. Plan: after the
  redesign, backtest "RSI above 50, no cap" against the current 50–70,
  prediction written first (Golden Rule 56). Switch only if it does as well
  or better, changing every copy together (Golden Rule 59). No change now.

- **Day 123 — Mean-Reversion Read card redesigned (mockup v0.10, pending
  sign-off).** Same pattern as the Technical Read: one big answer ("No
  signal" / "Buy the dip"), then "Buy the dip needs all four" tiles with
  ✓/✗ (RSI(2) below 10, above the 200-day average, price above $10, daily
  trading above $25M). On a signal, "The plan, exactly as tested": buy at
  tomorrow's open, stop 5% below the buy, sell on the first close with
  RSI(2) above 70, or after 10 trading days; no price target. Track record
  line: 241 trades, 70.5% wins, PF 2.00. Fixed in the mockup: No-signal
  panel used the green "favorable" colour and Signal used red.
  - **Bug found (to fix when the card is built):** the live
    `MRSignalCard.jsx` shows `detect_mr_signal()`'s stop (tighter of 5% or
    1.5 ATR) and target (entry + 2 ATR). Neither is the tested rule: the
    PF 2.00 ledger used a flat 5% stop, no target, RSI(2) > 70 or 10-day
    exit, entry at next open (`daily_job.py:87-90`, `mr_simulator.py`). The
    redesigned card shows only the tested rules.

- **Day 123 — Trade Setup card redesigned (mockup v0.11, pending sign-off).**
  - Two plans (Pullback: buy at support; Momentum: buy now), each with a
    risk/reward bar on one shared price scale (red = stop to buy, green =
    buy to target, "now" line), three fact tiles (Buy / Stop / Target with
    % and why), the reward:risk ratio, and a plain sentence ("Risk $12.68
    to make $15.80 a share"). Second state: at an all-time high the target
    is a projection, drawn dashed with "?".
  - No new pass/fail rules. One reference line gives the common rules of
    thumb (reward ≥ 2× risk; stop no more than 7–8% below the buy, O'Neil)
    without judging, because neither threshold exists in the engine
    (Golden Rule 59: a third R:R threshold on the page would disagree with
    the existing ones).
  - Card says plainly it is arithmetic, not a tested system (momentum
    failed every test; MR is the tested edge).
  - Mockup numbers corrected to the engine formula
    (`riskRewardCalc.js:30,36`): pullback stop = support − 2 ATR = $202.72
    (was shown as $208.90); momentum buy = today's $224.80 (was $225.10).
    Sizing card synced (stop distances 5.9% / 8.4%; RVOL 1.80 to match the
    Entry checks' 1.8×; ADX wording "moving sideways for now").
  - **Bug found (fix when built):** `riskRewardCalc.js:24` falls back to
    `currentPrice * 1.10` when there is no resistance target, a made-up
    number (Code Architecture Rule 6). The redesign shows the backend's
    projected target labelled as a projection, or no target.

- **Day 123 — Momentum plan and Sizing Inputs card removed (user-decided,
  mockup v0.12).**
  - Trade Setup shows only the pullback plan (buy at support, stop 2 ATR
    below, target nearest resistance). Reason: STA's own momentum system
    failed every backtest and the forward test (Path A PF 0.70, Path B
    retired). Breakout buying itself is canon (O'Neil); STA's version never
    earned its place. The pullback plan is untested by STA too, kept
    because it matches MR (the tested edge buys dips in an uptrend) and the
    canon low-risk entry.
  - Sizing Inputs card removed from the Analyze page. The Settings-tab
    position calculator stays as is.
  - **Build impact (Golden Rule 51/59):** `riskRewardCalc.js`'s
    `anyViable = pullbackViable || momentumViable` feeds the viability
    badge and the "⚠️ Stock not recommended" warning (`App.jsx:1691-1716`).
    When the momentum panel goes, those must stop counting momentum (or be
    removed with the old card), or the page could call a setup viable
    because of a plan it no longer shows. Removing the momentum panel also
    retires the hardcoded "half" position-size label bug (Day 109).

- **Day 123 — Fundamentals card redesigned (mockup v0.13, pending sign-off).**
  - Same pattern as the other cards: one answer ("No red flags" in plain
    text, never green; "⚑ 1 red flag" in amber; "Can't check"; "Not
    applicable" for ETFs), then three check tiles from
    `screenFundamentalRedFlags` (`categoricalAssessment.js:1114`): sales
    falling 10%+ a year, ROE below 0%, Debt/Equity above 2.0. Missing data
    shows dashed "no data / not checked" tiles so it never reads as "no
    flags" (§5 display rule).
  - New row: **next earnings date, always shown**, highlighted when within
    7 days (the existing `/api/earnings` warning window, `backend.py:1416`;
    no new threshold). Canon: O'Neil and Minervini avoid holding a fresh
    swing trade through earnings. Today the date only appears as a header
    badge inside 7 days.
  - Backing: sales decline and losing money match canon (O'Neil's
    growth/profit requirements) and Reddit; D/E above 2.0 is a common screen
    with a sector caveat (banks, utilities, REITs), stated on the card.
    Earnings growth (O'Neil's "C") stays out per the Day 119 decision.

- **Day 123 — P/E guide added to the Fundamentals card (user-requested,
  mockup v0.14).** Trailing P/E only, on a guide strip (under 15 / 15–25 /
  25+, labelled cheap / typical / priced for growth) with a plain sentence
  ("investors pay $38 for each $1 of yearly profit"). Never a flag, never
  coloured. Backing: O'Neil and Minervini found P/E doesn't predict the
  move (leaders often had high P/Es); Graham's "under 15 = cheap" is for
  long-term value investing; Reddit says compare to the sector and that a
  high P/E means bigger earnings reactions. No P/E = losing money. Data:
  `pe` already reaches the frontend (`api.js:93`). No sector average exists
  in STA, so no sector comparison.
  - **Bug found (Low):** `forwardPe` is mapped to Finnhub's
    `peBasicExclExtraTTM` (`field_maps.py:73`), which is a trailing P/E,
    not forward. Anything labelled "forward P/E" from Finnhub is wrong. The
    card uses trailing P/E only.

- **Day 123 — User signed off the full v0.14 design and said "start
  building".** Build order (amends the Day 119 plan's §E): Step 3 Trade
  Setup (pullback only; no Sizing grid; no momentum panel; no +10% target
  fallback), Step 4 Technical Read + Regime (adds score tiles and Entry
  checks; volume read moves here from Trade Setup), Step 5 MR card (new;
  tested rules only), Step 6 Fundamentals (adds P/E guide and earnings
  date), Step 7 default flip + Simple-view copy, Step 8 tests + docs. Built
  in the app's dark Tailwind theme with the mockup's layout. Each step is
  verified and shown to the user before the next.

- **Day 123 — Step 3 built: Trade Setup card (pullback plan only).**
  - New `frontend/src/components/PullbackPlan.jsx` (bar, Buy/Stop/Target
    tiles, plain sentence, reference line, "How this setup was formed").
  - `riskRewardCalc.js` reduced to the pullback plan; returns null target
    (not `price × 1.10`) when no resistance is found; `getViabilityBadge` /
    `hasViabilityContradiction` deleted (no other callers).
  - `App.jsx`: viability badge, "⚠️ Stock not recommended", advice banner,
    both entry panels (incl. the hardcoded momentum "half", Day 39) removed.
    Indicator chips (ADX / 4H RSI / OBV / Vol / ⚠️ DIST) kept unchanged as a
    row under the plan; the Day 111/116 volume block, S&R levels and MTF
    unchanged. Step 4 decides the chips' and volume block's final home.
  - Verified: `npm run build` clean (only the 6 pre-existing warnings);
    live NVDA renders (support $164.27 − 2×ATR $8.70 = stop $146.87,
    target R1 $188.00, 1.4 : 1); edge cases unit-checked (projected target,
    no target → no ratio, no support → message, $0.01 stop floor). Simple
    view's entry/stop unaffected (reads backend `suggestedEntry/Stop`).
    Not yet seen live: an all-time-high ticker. `ui-verify-checklist.js`
    still asserts the removed panels — rewritten in Step 8 as planned.

- **Day 123 — Engineering standard adopted (user).** Every step from now:
  a written plan reviewed by an independent Opus/Fable agent before code;
  no silent failures; logging; helpers that never throw; every UI element
  backed by real backend data; logic true to the engine. Plan:
  `ANALYZE_REDESIGN_STEP4_PLAN_DAY123.md` (Fable: GO WITH FIXES, all 14
  findings accepted, §7).

- **Day 123 — Step 3 hardened + Step 4 built (Technical Read + Regime).**
  - Silent failures fixed: failed `/api/sr` no longer hides the Trade Setup
    card (it says "Couldn't load support and resistance levels");
    `calculateRiskReward` returns an explicit state (`no_data` /
    `no_support` / `no_atr` / `ok`) instead of `atr || 0`; backend
    `suggestedStop` is null with a logged warning when ATR is missing (was a
    made-up 3% stop the Simple view showed and sized from; the Simple
    Checklist setup criterion now falls to its existing support-distance
    branch in that case); backend RVOL is None, not a made-up 1.0, when the
    50-day average volume is 0; `prevBar.date` labelled yesterday's bar with
    today's date while today's bar was forming (fixed:
    `df.index[-2]` always); trend template missing is logged with bar count.
  - New: `RegimeRead.jsx` band, `TechnicalRead.jsx` card (read + ADX
    "taking a breather"; 4 trend checks with labels that follow pass/fail;
    "Strong needs all three" tiles from `deriveStrongCriteria`, which reads
    the new shared `STRONG_RULE` constants that `assessTechnical` now also
    uses; Entry checks: timing vs 21-day EMA in ATR, 20 volume bars with the
    backend's own 50-day average definition and partial-bar outline, 3 votes,
    distribution warning), `technicalReadChecks.js`, `useMissingInputWarning`
    hook (`[STA][card]` console warnings).
  - Removed from the Full view: BUY/HOLD/AVOID badge and T/F/S/R row in the
    header (Simple view and Assessment Breakdown keep theirs), the indicator
    chip row (ADX → read line; OBV/Vol/DIST → Entry checks; 4H RSI dropped),
    5 dead functions. The Day 111/116 volume read moved unchanged into
    Entry checks' "Volume detail".
  - RS tile shows both 52-week returns ("+43% vs +10%"), never
    `(ratio − 1) × 100`; ✓ stays on ratio ≥ 1.0 (equivalent test).
  - **Engine bug logged (not fixed in Step 4):** a missing RSI becomes 50
    (`runCategoricalAssessment`, `assessTechnical`) and counts as a pass
    toward Strong. The card now says "RSI didn't load; the engine assumed
    50". Fixing it changes verdicts, so it needs its own parity-tested change.
  - Verified: build clean (only the pre-existing ValueTab warning; 5 dead-
    function warnings gone); verdict parity 86,400/86,400; 26 Node unit
    checks incl. a 112-combo grid proving tiles == engine Strong call; live
    NVDA (Weak), AVGO, GOOGL (Weak), LLY (Strong, extended, projected
    target "?"), SPY (Developing, ADX breather, below EMA), bad ticker
    (explicit error), forced `/api/sr` failure (every section says why, one
    `[STA]` warning per card), 390px mobile (no overflow in the new cards;
    the app's tab bar/Analyze button overflow at 390px is pre-existing).
  - Known breakage (Step 8): `ui-verify-checklist.js`,
    `ui-cohesiveness-test.js` scrape the removed verdict badge / T:X row.
  - **Code review (Fable) fixes, same day:** no MUST-FIX. Applied: Price
    Structure's fake `?? 1.0` RVOL removed; Regime band says "SPY trend
    unavailable" instead of "downtrend" when SPY data is missing (**second
    engine bug logged:** `assessRiskMacro` treats missing SPY as below its
    200-day → Unfavorable); young tickers say "under a year of history"
    not "try again"; backend `candle.date` so a past session is never
    labelled "Today"; Simple Checklist setup fails visibly with no stop.
    34 Node checks, parity green, build clean, live LLY/NVDA/SPY re-checked.

- **Day 123 — Step 5 built: Mean-Reversion Read card (tested rules only).**
  - **Finding (Fable plan review, verified):** the forward test's PF 2.00
    priced every trade at the entry day's CLOSE (`daily_job.py` replay via
    `simulate_mr_trade`, `mr_simulator.py:69`), although the ledger recorded
    the open. User chose: card plan = buy at the next open; re-test the
    forward trades on that basis. Prediction pre-registered (PF 1.5–1.7, WR
    63–68%). Result (`backtest/mr_open_entry_retest.py`, all trades, same
    data both bases): **broad 241 trades: close PF 2.40 → open PF 1.50, WR
    63.5%, +0.70%/trade; HUB-65 70 trades: open PF 1.07, +0.16%/trade.**
    Prediction held at the bottom edge. Ledger also holds a fake MNST −50.8%
    (split artifact). PF 2.00 to be corrected wherever quoted (session close).
  - Backend: `market_time.py` (one forming-bar rule, cutoff 16:30 ET to match
    the OHLCV cache expiry; S&R and MR routes use it), `MR_RULES` single
    definition (frozen simulator/daily_job values asserted equal by
    `backtest/test_mr_rules.py`), `detect_mr_signal` tri-state conditions
    with `missing`, ATR stop / +2 ATR target / 2% ATR fallback removed,
    `/api/mr/signal` drops the forming bar before the 200-bar check and
    returns `asOf`, `barDropped`, `dataSource`, `trackRecord` (from the
    re-test file + ledger dates), scan rows carry `asOf`.
  - Frontend: `MRRead.jsx` replaces `MRSignalCard.jsx` (deleted); always
    shown (loading / couldn't check (reason) / No signal / Buy the dip);
    4 rule tiles (no-data tiles dashed); clock-aware entry line
    (`mrEntryTiming.js`: says when the tested open has already passed);
    track record per universe with its own dates + backtest PF 1.16;
    moved under the Technical Read. Scan tab MR rows show the tested plan,
    not the old stop/target. `fetchMRSignal` returns `{error, reason}`.
  - Verified: 21 Python checks, 8 timing checks, build clean, parity green,
    live XOM (signal, open already passed), NVDA (no signal: below 200-day),
    forced failure, 390px, Scan tab MR list. Fable code review: 1 MUST-FIX
    (HUB-65 shown with broad dates) + 8 smaller, all fixed.

- **Day 123 — Holding Period, Assessment Breakdown and BUY/HOLD/AVOID removed
  (user-decided).** Holding period's only consumer was `determineVerdict`'s
  tech/fund weighting; the Breakdown repeated cards that now exist. User
  chose "BUY/HOLD/AVOID everywhere": removed from the Analyze page, the
  Simple view comparison strip, and the Scan tab's Day 106 STA Verdict
  column. Engine code + parity test untouched; verdict still computed at a
  fixed 'standard' horizon for the trade journal's stored field.

- **Day 123 — Step 6 built: Fundamentals card + removals.**
  - New `FundamentalsRead.jsx` + `fundamentalsRead.js`: three red-flag
    tiles (sales, return on equity, debt; thresholds from
    `RED_FLAG_THRESHOLDS`), P/E guide (never a flag; "P/E not reported"
    unless negative — no profitability inference), next earnings always
    shown (backend `daysUntil`/`hasUpcoming`, highlighted in the 7-day
    window), "Can't check" vs "No red flags" vs "Not applicable" (ETF via
    yfinance `quoteType`, engine list, or name fallback), per-field data
    sources, negative-equity D/E shown as not meaningful.
  - **Data bugs fixed (Fable plan review):** yfinance D/E was in percent
    (AAPL ≈154 would have been flagged); yfinance/FMP ROE ≥100% showed as
    "1.5%". Both also skewed `assessFundamental`. Fundamentals cache schema
    v2 → v3. Earnings `days_until` was off by one (−1 on the day itself);
    now New York calendar days via `calendar_days_until`, timestamps
    converted to NY time, and "every source failed" returns unknown instead
    of "no date found". Alpha Vantage sales basis is quarterly YoY (FMP is
    the annual one).
  - Removed: Holding Period selector + effect, Assessment Breakdown +
    `AssessmentTile.jsx`, Raw Indicators, Quality Gate Warnings (their
    content: 200 SMA/RS in the Technical Read, liquidity in Price & RS),
    fundamentals-unavailable banner (now the card's "Can't check"), Simple
    view comparison strip, Scan STA Verdict column, dead state/helpers.
  - Verified: 27 Node + 13 Python checks, parity 86,400/86,400, build clean,
    live AAPL / NVDA / RIVN (⚑ negative ROE) / JPM (⚑ D/E 3.32, bank caveat)
    / SMH / SPY / forced fundamentals failure; no BUY/HOLD/AVOID verdict in
    the Full view. Fable code review: 2 MUST-FIX + 8 smaller, all fixed.
  - Step 8 cleanup candidates: scoringEngine still computes `qualityGates`
    nothing renders.

- **Day 124 — Step 7 built (plan: `ANALYZE_REDESIGN_STEP7_PLAN_DAY124.md`).**
  User decision: no market verdict; the Regime band became the "Market
  backdrop" card (S&P 500 and Nasdaq-100 long/short-term trend, biggest
  1-day drop in 10 sessions, VIX), first on the page. Full Analysis is the
  default view; Simple says "⏸️ No Trade". ETFs say "Exchange-traded fund
  (ETF)". Follow-up the same day: one VIX band wording on every screen
  (`backend/vix_bands.py`), honest MR next-open figures on Forward Test,
  backdrop → Context link.

- **Day 124 — Step 8 built: tests, cleanup, docs. Redesign complete.**
  Plan: `ANALYZE_REDESIGN_STEP8_PLAN_DAY124.md` (Fable: GO WITH FIXES, all
  10 findings accepted, §5; build notes §6).
  - `ui-verify-checklist.js` rewritten: 8 checks (A1–A6, A8, A9) in a pure,
    unit-tested module (`scripts/lib/analyzeChecks.js`, 66 checks); compares
    the screen with the exact JSON the page received; new dated report
    folder per run; exit 1 on any failure. `ui-cohesiveness-test.js` fixed
    (card hooks, no holding period, new manual checklist).
  - Stable `data-testid` hooks on every card (no visible change).
  - The two inline VIX position-size ladders now call
    `getVixPositionMultiplier`; the calculator says "VIX not loaded" instead
    of silently using 1.0×.
  - `qualityGates` / `checkQualityGates` removed from scoringEngine.
  - Day 119 Phase 6 Scan-tab disclosure line: moot (column removed Step 6).
  - Verified: 5 tickers 40/40 live, two deliberate breaks both caught,
    parity 86,400/86,400, build clean apart from the old ValueTab warning.
