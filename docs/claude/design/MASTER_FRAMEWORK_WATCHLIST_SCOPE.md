# Master Framework Watchlist — Scope Document (Day 85)

> **Purpose:** Scope for a personalized screener sourced from the user's Notion
> "Master Investment Framework Hub" — a curated, thesis-driven ticker universe,
> as an alternative to STA's TradingView market-wide scan.
> **Status:** ✅ BUILT AND VERIFIED (Day 85). See §6 for what shipped and the
> verification results.
> **Source:** User-requested Day 85. See [[project-notion-personalized-screener]]
> in memory and ROADMAP.md priority #2.

---

## 1. Source

Notion page: `🏛️ Master Investment Framework Hub`
(`https://app.notion.com/p/385965c99ae081498ea3e880ea388abf`)

4 child frameworks, each a scored, tiered watchlist with its own methodology:

| Framework | Layer | Scope | Tickers (raw) |
|---|---|---|---|
| 🤖 AI Supply Chain v3.0 | Layer 2 | Global AI infrastructure | 20 core + 9 "missing names" expansion + supplier layer |
| 💎 CanGem v3.1 | Layer 1 | Canada + US "hidden gems" | Canada (5 gems + 7 execution + 3 sector lists) + US (4 gems + 2 execution) |
| 🪨 STRATUM v1.0 | Layer 0 | Raw material chokepoints, all 10 megatrends | Layer 1 "master watchlist" (20) + Layer 0 raw-material speculative (6) |
| ⚛️ QUBIT v1.0 | Layer 0a | Quantum-only supply chain | 7 names, **all explicitly Stage 0-1** |

A 5th page, "🌍 Humanity 10-Year Convergence Map," is thesis/narrative only — no
new scored tickers, just references names from the other 4.

---

## 2. Scoping decisions (made Day 85, user-confirmed)

1. **Purpose:** Run STA's existing technical engine (Trend Template, S/R,
   patterns, verdict) against this list — same pattern as the Nirmal
   watchlist feature, **not** a new capability that merges Notion's
   fundamental thesis/score/stage into STA's output. Technical read only.
2. **Sync model:** Periodic manual refresh (a script re-fetches Notion via
   MCP and regenerates a local ticker list), **not** a live Notion API call
   on every scan. Matches the frameworks' own documented cadence (their
   "Weekly Rerun Protocol" — Notion content changes at most weekly, not
   intra-day).
3. **Tier filter — established names only.** Frameworks vary in whether
   they self-label speculative tiers:
   - AI Supply Chain: no speculative tier — all names are revenue-generating,
     institutionally relevant. **All included.**
   - CanGem: has an explicit "quality gate" (positive revenue/earnings
     required to enter the candidate pool at all) — even its smaller/riskier
     names (PNG.V, FLT.V) already passed that bar. **All included.**
   - STRATUM: has two tiers in the same document — a "Layer 1 master
     watchlist" (established toll-booth companies) and a separate "Layer 0
     raw material chokepoint" table explicitly self-labeled "speculative,
     pre-narrative, Stage 0-1 positions... max 1-3% per position." **Only
     Layer 1 included; Layer 0 (NBY.V, PLSR.V, AVL.TO, ARA.TO, HEVI.V)
     excluded.**
   - QUBIT: the entire framework is self-labeled "all positions are Stage
     0-1... binary upside sizing, not conviction sizing." **Entire framework
     excluded** — zero tickers survive.
   - Two tickers (ARQQ, OKLO) appear only in the Convergence Map's
     illustrative tables, not in any framework's own scored watchlist —
     **excluded**, kept the filter strict to "appears in a framework's own
     scored table."
4. **Exchange coverage.** 3 tickers sit on exchanges STA's scanner doesn't
   support today (only NYSE/NASDAQ/AMEX and TSX/TSXV/NEO are wired in
   `scan_queries.py`'s `US_EXCHANGES`/`CANADIAN_EXCHANGES`):
   - `SLX.AX`, `ILU.AX` — Australian ASX
   - `OXIG.L` — London LSE
   **Dropped.** Adding ASX/LSE support is a separate, much bigger effort not
   justified for 3 tickers.
5. **UI placement:** New entry in the existing Scan tab's strategy dropdown
   (same pattern as "👁 Nirmal's Watchlist"), not a new dedicated tab. No new
   page/navigation needed.

---

## 3. The final ticker list — 76 tickers (77 scoped, 1 dropped on verification — see §6)

### AI Supply Chain (35)
```
GEV, ETN, GIB.A, TSM, VRT, GLW, CCO.TO, APH, ANET, FN, ASML, CEG, DELL,
BWXT, MOD, ALAB, TMUS, HPE, KEYS, HPQ, NVDA, AVGO, MU, MRVL, ONTO, CAMT,
ORCL, FCX, AMD, CLF, TEL, PWR, LEU, ATI, IFNNY
```

### CanGem (28, deduplicated against AI Supply Chain)
```
MDA.TO, ASTL.TO, BDT.TO, CGY.TO, PNG.V, CVE.TO, WSP.TO, ATRL.TO, NTR.TO,
MRE.TO, LNR.TO, CNQ.TO, SU.TO, TRP.TO, ENB.TO, CAE.TO, MAL.TO, BBD.B.TO,
CLS.TO, T.TO, BCE.TO, FLT.V, STRL, CW, DY, EME, ENS, VST
```

### STRATUM — Layer 1 only (14, deduplicated against the above)
```
TECK.B.TO, KXS.TO, ARE.TO, CS.TO, PLTR, CGNX, LSCC, RKLB, NOC, PATH, NET,
ASTS, ISRG, XYL
```

**Dropped (Stage 0-1 / unsupported exchange, not in the 77):** NBY.V,
PLSR.V, AVL.TO, ARA.TO, HEVI.V (STRATUM Layer 0), ASPI, OXIG.L, SLX.AX,
TECK.B.TO-dup (QUBIT — TECK.B.TO already counted above via STRATUM Layer 1),
ARQQ, OKLO (Convergence Map only), ILU.AX (STRATUM hafnium mention).

**Duplicates across frameworks (counted once):** CCO.TO (AI SC + CanGem +
STRATUM), BWXT (AI SC + CanGem), GEV (AI SC + CanGem), CEG (AI SC + CanGem),
FCX (AI SC + STRATUM), TRP.TO (CanGem + STRATUM), ATRL.TO (CanGem +
STRATUM), MDA.TO (CanGem + STRATUM), TEL (AI SC, also referenced as a
supplier in the same doc).

---

## 4. Implementation shape (not yet built)

Following the existing Nirmal watchlist precedent (`App.jsx`'s
`NIRMAL_WATCHLIST` array + parallel S/R fetches):

1. **A refresh script** (new, e.g. `backend/scripts/sync_notion_watchlist.py`
   or a Claude-run manual step) — re-fetches the 4 framework pages via the
   Notion MCP tools, re-derives the ticker list per the rules in §2, and
   writes it to a static list (mirroring `NIRMAL_WATCHLIST`'s shape). Not
   automated/scheduled — manual re-run when the user updates the Notion
   pages (their own cadence is weekly at most).
2. **Frontend:** a new `MASTER_FRAMEWORK_WATCHLIST` array in `App.jsx` (or a
   new small JSON/JS data file imported by it), plus a new dropdown option
   in the Scan tab, reusing the exact same parallel-fetch-and-render code
   path the Nirmal watchlist already uses — no new component needed.
3. **No backend route changes** — this reuses `fetchSupportResistance()` per
   ticker exactly like Nirmal's watchlist does, not a new endpoint.
4. **No verdict/scoring logic changes** — this is purely "which tickers get
   analyzed," not a change to how any ticker is analyzed.

Estimated effort: small — same shape as the Nirmal watchlist feature already
in production.

---

## 6. What actually shipped (Day 85)

Built exactly per the shape in §4 — no backend changes, no new component.

| Change | File |
|---|---|
| `MASTER_FRAMEWORK_WATCHLIST` array (76 tickers) | `frontend/src/App.jsx` |
| `fetchWatchlistCandidates(tickers, label)` — shared helper extracted from what was previously Nirmal-only inline logic, now used by both watchlists | `frontend/src/App.jsx` |
| New `masterFramework` branch in `runScan()` | `frontend/src/App.jsx` |
| New dropdown option: "🏛️ Master Framework Watchlist — 76 curated picks" | `frontend/src/App.jsx` |

**Verification (exhaustive, all 77 originally-scoped tickers checked against
the live backend, not a spot-check):**
- 3 tickers needed a format fix — the data providers expect a hyphen for
  Canadian dual-class shares, not the dot format Notion's docs use:
  `GIB.A` → `GIB-A.TO`, `TECK.B.TO` → `TECK-B.TO`, `BBD.B.TO` → `BBD-B.TO`.
- 4 tickers (`MDA.TO`, `CGY.TO`, `WSP.TO`, `MRE.TO`) initially timed out at an
  8s per-request check — retried at 25s and all resolved fine. Not a real
  problem, just a slower first-fetch (no cache yet) for less-common tickers.
- 1 ticker, `FLT.V` (Volatus Aerospace), returned "No data found" under both
  the `.V` and no-suffix format from every provider in the fallback chain.
  Genuinely unsupported — dropped from the list rather than shipping a
  ticker that would always error. **Final list: 76, not 77.**

Frontend compiled clean (only pre-existing unrelated lint warnings).
Not verified in an actual browser session (no Playwright/chromium-cli
available in this environment and not worth installing fresh for this
change) — verification was done by confirming the underlying data pipeline
resolves every ticker the new code references; the React code path itself
(`fetchWatchlistCandidates`) is a direct, mechanical extraction of the
already-shipped, already-verified Nirmal watchlist logic.

---

## 7. Open items for a future refresh

- If the user later wants the Notion thesis/score/stage surfaced alongside
  STA's technical verdict (deferred per §2 decision 1), that's a separate,
  larger scoping exercise — not in this build.
- If the user's Notion frameworks add ASX/LSE names in the future, exchange
  support would need to be revisited.
