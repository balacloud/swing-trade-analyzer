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
> **Last Updated:** Day 109

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
**Status:** Locked — split from the composite verdict badge into its own
element (resolved via AskUserQuestion, Recommended option: "Split into two
elements").

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

**Page subtitle** (under the ticker):
> Independent reads, shown side by side. You make the call.

**Regime band** (new element, always visible, three states):
> 🟢 **Regime: Favorable** — VIX 16.4, SPY above its 200-day SMA.
>
> 🟡 **Regime: Neutral** — VIX 24.1 (elevated), SPY above its 200-day SMA.
> Proceed with reduced conviction.
>
> 🔴 **Regime: Unfavorable** — SPY below its 200-day SMA. **This is a
> stand-down regime regardless of how good an individual setup looks.**
> Capital preservation before growth — the one rule on this page that is
> deliberately not left to judgment.

**Technical Read chip:**
> **Technical Read: Strong** · Trend Template 8/8, RSI 65.9, RS 1.03
>
> **Technical Read: Strong · trend not yet confirmed (ADX 14.2)** ← ADX<20
> modifier
>
> **Technical Read: Unavailable** — pattern detection didn't return for
> this ticker

**R:R below-1.0 note** (muted, teal-bulleted, same grammar as Price
Structure's watch items):
> • R:R is 0.34 because the nearest resistance (R1 $227.49) is only 1.0%
> above price while the ATR-based stop sits 7.1% below. The constraint is
> target proximity, not stop placement.
>
> • This ratio is computed from the S&R levels shown above. Those levels
> come from a pivot method that selects the most price-extreme levels in
> range, not the nearest ones — a known open issue (Day 108). Read the
> number as one input, not a verdict.

**R:R footnote** (persistent, replaces any "3 thresholds" framing — see §3
correction 2):
> **Note on the R:R numbers on this page.** Three different quantities are
> labeled R:R here and they are not comparable. The two entry panels use
> ATR-based stops (2×ATR for pullback, 1.5×ATR below support for momentum).
> "R:R Context" in the setup banner is a ratio of percentage distances to
> support and resistance — no stop, no ATR. The Pattern Detection card's R:R
> uses a fixed target multiple (1.12-1.20× pivot), not real resistance. All
> three are shown; none gates anything.

**Sizing inputs grid** (header + framing):
> **Sizing inputs** — the raw numbers, no recommendation. Position sizing is
> roughly 90% of a system's results (Van Tharp); it's the last thing this
> page will decide for you.
>
> [ADX] [ATR] [Stop distance — pullback] [Stop distance — momentum] [RVOL]
> [VIX]
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
>
> ⚑ **1 red flag** — Revenue declining −12.4% YoY.
>
> Screen unavailable — fundamentals data didn't return for this ticker.
>
> Not applicable — ETF.
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

**Scan tab disclosure line** (one line under the "STA Verdict" column
header, per item 12's cross-tab resolution):
> Scan-tab verdict uses the frozen backtested BUY/HOLD/AVOID tree, the same
> engine the paper-trading tracks are pre-registered against. The Analyze
> page's read is a separate, display-only summary.

---

## §7 — Implementation plan

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
| Negative-EPS red flag | A live-payload check of what `epsGrowth` actually contains (growth rate vs. level) | Golden Rule 3 — don't assume structure before verifying |
| Pattern Detection card's fixed-multiple R:R caveat | A one-line honesty note, same family as §6's R:R footnote | Low effort, not yet scheduled — flagged in item 11's entry |
| `/api/sr/<ticker>`'s duplicate backend/frontend R:R arithmetic (item 8) | Post-freeze DRY cleanup | Touches `backend.py`'s S&R route, upstream of `compute_sr_levels` — deferred, not urgent |
| No visual mockup built yet | Build the Artifact once remaining copy/threshold questions are closed | User explicitly asked for decisions to finalize before the mockup, not in parallel |
| ROADMAP.md priority entry for this work | Add during §7.6 (docs phase) if/when implementation starts | Not yet added — this design doc exists independently of the roadmap today |

---

## §10 — Change log

- **Day 109:** Document created. 13 items locked via iterative Q&A
  (user-driven), validated and corrected by a dedicated Opus review pass (4
  corrections, 4 additional decisions resolved: default view, ADX modifier,
  Technical Read/Regime split, evidence-based red-flag thresholds). Full
  implementation plan drafted, not executed. No application code changed.
