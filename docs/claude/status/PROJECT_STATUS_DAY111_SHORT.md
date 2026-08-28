# Project Status — Day 111

## Version: v4.59 → v4.60 (Backend v2.47 → v2.48, Frontend v4.54 → v4.55)

---

## What Happened Today

The longest single session in the project's history — a full technical audit
of five Analyze-page cards, a complete data-provenance map of the app, two
real features shipped and verified live, and two forward-test tracks
crossing their 100-trade confirmation bar with sharply different results
under scrutiny. Seven visual Artifacts published. Two real code changes
actually shipped; everything else is design/plan/documentation.

### 1. Deep technical audit — S&R, MTF Confluence, Price Structure, Pattern Detection, Breakout Status

Graded all five against real, named industry methodology (not a vibe):
Price Structure and Breakout Status both **9/10** (genuinely well-built,
matches published Dow Theory / institutional breakout-confirmation
standards); Pattern Detection's recognition logic **8/10** (matches
Minervini/O'Neil's published VCP/Cup&Handle/Flat Base criteria) but its
price target **1.5/10** (a flat percentage, never checked against real
resistance); MTF Confluence **3/10** (the Day 108 critical bug is fixed,
but its confidence score is an arbitrary hardcoded multiplier); Support &
Resistance **2/10** — the pivot method's "nearest support" selection
actually picks the most *extreme* level in range, not the nearest one,
confirmed by direct code read. **New Golden Rule 53.** Full remediation
plans (not yet implemented) written for all three below-standard findings
in `KNOWN_ISSUES_DAY111.md`.

### 2. Full data-provenance map + 2 real fixes shipped

Mapped every tab to its actual data source — four separate systems, not
one pipeline (the multi-provider orchestrator, TradingView's screener,
FRED, and direct scrapes). Found 5 findings (`DATA_PROVENANCE_FINDINGS_DAY111.md`):
two batch endpoints bypass the orchestrator's circuit-breaker protection
with zero Tradier fallback; `/api/mr/scan` inconsistently bypassed the
orchestrator when its sibling endpoint didn't (**fixed**); Tradier's real
capacity sits unused in exactly the scenario that's already caused a rate-
limit incident (Golden Rule 25); the Data Sources tab's own field-source
documentation was stale ("Defeat Beta API," a provider no longer in any
active chain); a consolidated list of dead fundamentals-related code.

### 3. MR Scanner wired to the Scan tab — SHIPPED

`fetchMRScan()` and its backend endpoint `/api/mr/scan` had existed,
fully built, completely disconnected from the UI since Day 81. Added a
"🔄 MR Signals" button to the Scan tab, its own results panel, click-through
to Full Analysis. Fixed `/api/mr/scan`'s orchestrator bypass in the same
pass, since it was about to get real traffic. **Verified live in browser:**
54-ticker scan, ~20s, 7 real signals returned, click-through confirmed
working. Along the way, found and restarted a genuinely stuck backend
(unresponsive even to `/api/health` after 2 weeks of uptime) — unrelated
to this change, a known class of issue for this project's dev server.

### 4. Volume Confirmation + Direction — SHIPPED, two-phase build

**Phase 1 (magnitude):** the Day 107 "volume confirmation" gap — previously
tested as a hard gate (Config F), cut trades 75→5, abandoned as too strict —
redesigned to match this project's own established fix for exactly this
failure shape (Fundamentals/R:R/Regime all hit the same wall and were moved
from gate to Info). Opus-planned first, which corrected two wrong premises
in the original brief (RVOL wasn't on a "Sizing Inputs grid" — that only
exists in the unimplemented redesign mockup; the "shared 1.5x threshold"
was actually 7 unlinked copies, two with false "shared" comments). Shipped
on the live Trade Setup card: new `frontend/src/utils/volumeThresholds.js`,
de-duplicated `priceStructureNarrative.js`'s copy of the constant.

**Phase 2 (direction):** extended with a directional lean — combining day's
price change, close-location-in-range, and OBV trend into an honest
"leans toward buying/selling pressure" or "mixed signals, no clear lean."
Opus-planned again, which found a real, separate, pre-existing bug along
the way: OBV's trend classification is structurally biased toward
reporting "rising" whenever cumulative OBV is negative (a sign-comparison
quirk) — logged, not fixed (touches a shipped, live badge; needs its own
review). New backend field `meta.candle` on `/api/sr/<ticker>` (additive).
**Verified live on real tickers**, including the hardest case: TSLA's
three signals genuinely disagreeing, correctly rendering "mixed signals,
no clear lean" rather than being averaged away or hidden.

### 5. Two forward-test tracks crossed their 100-trade bar — very different outcomes under scrutiny

**MR (broad): genuinely confirmed.** 138 closed trades (105 at first
check this session), 79.71% WR, PF 3.0021. Stress-tested the same way
every MR milestone gets tested here: even excluding its single largest
cluster (3 consecutive days, 38% of the sample), PF held at 2.24 and win
rate actually *rose* to 80%. The edge is not the cluster.

**Momentum Path B: fails the same test, badly.** 117 closed trades,
50.43% WR, PF 1.2293 — technically clears the pre-registration's own
"Confirmed" bar (§10: PF≥1.2, positive expectancy, ≥100 trades). But
**66.7% of its entire closed sample (78 of 117 trades) entered in a single
4-day window, Aug 3-7.** Excluding just those 4 days: 39 trades remain,
43.6% WR, **PF 0.72 — net losing**, well into the pre-registration's own
"Broken" tier (<0.9). The cluster isn't sector-concentrated (checked —
wide mix of energy, healthcare, financials, tech, consumer names), so this
isn't the already-known sector-correlation gap; it's a *regime/timing*
correlation instead — the entry gate fired heavily during one specific
market window and the whole track's statistics ride on it. **Not treating
this as confirmed.** Full writeup in `KNOWN_ISSUES_DAY111.md`; new
PERSONA.md Feedback Log entry.

MR HUB-65 also growing (33→49 closed this session), not yet at its bar.

### 6. Session organization

Built `docs/claude/stable/AUDIT_COVERAGE_LEDGER.md` (tracks last-reviewed
date/depth for all 11 app components — the direct answer to "how do I know
if a future review is finding something new or just re-surfacing
something already known") and `docs/claude/design/SESSION_ARTIFACTS_INDEX_DAY111.md`
(catalogs all 7 Artifacts published this session with an honest current-
state note on each — 3 fully current, 2 with one known-stale point, 2
about the same subject and both lagging the same source doc slightly).

### 7. Open, unresolved — flagged explicitly, not silently dropped

**The S&R fix itself was scoped but not started.** Before any code was
written, found that `support_resistance.py`'s `_pivot_sr()` — the function
with the confirmed extreme-vs-nearest bug — is not just Analyze-page
display support; Momentum Path B's live entry gate imports
`compute_sr_levels()` directly and gates real trades on it. Per Golden
Rule 18, fixing it in place would reset Path B's count. Given Path B's own
result this session (see #5), that tradeoff looks different than it did
an hour earlier — but the decision itself is still explicitly pending, not
made. **New Golden Rule 54.**

---

## Files Changed

| File | Change |
|---|---|
| `backend/backend.py` | `/api/mr/scan` orchestrator fix; new `meta.candle` field on `/api/sr/<ticker>` |
| `frontend/src/utils/volumeThresholds.js` | New file — volume magnitude + direction reads |
| `frontend/src/utils/priceStructureNarrative.js` | De-duplicated `BREAKOUT_VOLUME_THRESHOLD`, now imports shared module |
| `frontend/src/App.jsx` | MR Scanner button + results panel; Volume Confirmation + Direction note on Trade Setup card |
| `docs/claude/stable/GOLDEN_RULES.md` | +2 rules (53, 54) |
| `docs/claude/stable/AUDIT_COVERAGE_LEDGER.md` | New |
| `docs/claude/design/SESSION_ARTIFACTS_INDEX_DAY111.md` | New |
| `docs/claude/versioned/DATA_PROVENANCE_FINDINGS_DAY111.md` | New |
| `docs/claude/versioned/KNOWN_ISSUES_DAY110.md` | Multiple updates through the session (superseded by `KNOWN_ISSUES_DAY111.md` at close) |
| `docs/claude/design/ANALYZE_PAGE_REDESIGN_DECISIONS.md` | §6 plain-English copy, §9 new items, item 15/16 updates |
| `docs/claude/stable/PERSONA.md` | New Day 111 Feedback Log entry |
| 7 Artifacts published/updated | See `SESSION_ARTIFACTS_INDEX_DAY111.md` |

---

## All Gates Status

| Track | Open | Closed | WR | PF | Status |
|---|---|---|---|---|---|
| Momentum Path A (frozen) | 25 | 59 | 52.54% | 1.5799 | Accumulating, <100 |
| Momentum Path B | 61 | 117 | 50.43% | 1.2293 | **Crosses numeric bar, fails cluster stress-test — not treated as confirmed** |
| MR (broad) | 20 | 138 | 79.71% | 3.0021 | **Confirmed — survives cluster stress-test** |
| MR HUB-65 | 2 | 49 | 61.22% | 1.661 | Accumulating, <100 |

**Freeze status:** unchanged — forward-testing accumulation remains the
sole stated priority. MR (broad) being genuinely confirmed is the first
track in the project's history to clear this bar for real.

---

## Next Session Priorities

1. **Decide the S&R fix scope** — the single most important open decision.
   Three options on the table (fix in place and accept Path B's count
   reset; parallel-track it like Path B itself was built at Day 95; scope
   to display-only). Given Path B's own result this session, "accept the
   reset" now looks materially less costly than it did before — worth
   weighing that explicitly, not defaulting to the safest-sounding option.
2. **Decide what Path B's cluster finding actually means for the track.**
   Not addressed this session beyond documenting it. Does it change
   anything about how Path B is treated going forward, or does it just
   sit as a caveat until 100 more trades average it out?
3. Once the S&R decision is made: Opus-plan, then Sonnet-implement, same
   process as the two shipped features this session.
4. Pattern Detection's Cup & Handle / Flat Base price-target fix — no
   dependency on the S&R decision, can ship independently anytime.
5. MTF Confluence's arbitrary-multiplier fix — same, independent.
6. Small cleanup batch, zero risk, any order: delete the 3 dead
   `App.jsx` functions (Forward P/E landmine), fix the Data Sources tab's
   stale provider documentation, Value Tab's investor-name relabeling.
7. OBV trend sign bug — needs its own review, touches a shipped live badge.
8. Mockup's Regime band still shows pre-Day-110-reversal copy — one-line
   fix, flagged, not yet done.
9. The bigger question, still open from before this session: does the
   full Analyze Page Redesign become a real implementation project, or
   stay a well-documented reference that gets cherry-picked from (as
   happened twice this session)?
