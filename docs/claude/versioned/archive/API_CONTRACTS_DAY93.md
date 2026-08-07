# API Contracts — Day 93 (July 22, 2026)

> Only documents what changed this session. For the full endpoint reference, see the most recent complete contract doc plus this file's additive delta.

## Changed: `GET /api/sectors/rotation`

**Additive only — no fields removed or renamed.**

Two new top-level fields added to the response:

| Field | Type | Description |
|---|---|---|
| `macro_alignment` | `string \| null` | One plain-English sentence stating whether the current macro backdrop (the same 10-indicator `overall_regime` computed by `/api/context/<ticker>`) supports the sector rotation being shown. `null` if the underlying cycles/econ read fails (fail-silent — the rest of the sector data still returns normally). |
| `macro_alignment_status` | `'aligned' \| 'cross_current' \| 'neutral' \| null` | Machine-readable status behind the sentence above. `aligned` = macro FAVORABLE + ≥1 sector Leading. `cross_current` = macro ADVERSE + ≥1 sector Leading (price running ahead of fundamentals). `neutral` = everything else (including macro NEUTRAL, or no sector Leading at all). |

**Implementation notes:**
- Computed only on cache-miss (once per trading day, same cadence as the rest of this endpoint's response) — not per-request.
- Reuses the existing FRED-cached `/api/cycles` and `/api/econ` engines (6h TTL) via a shared `compute_overall_regime()` helper (also used by `/api/context/<ticker>`) — **no new Alpha Vantage or yfinance calls**. Deliberately does not call `/api/context/<ticker>` itself, which would burn Alpha Vantage's news quota on a placeholder ticker every time this cache goes cold.
- Wrapped in its own try/except — if the cycles/econ read fails for any reason, `macro_alignment`/`macro_alignment_status` are `null` and the rest of the sector rotation response is unaffected.

**Consumer:** `frontend/src/components/SectorRotationTab.jsx` renders this as one line under the tab's existing plain-English takeaway sentence. `frontend/src/services/api.js`'s `fetchSectorRotation()` was updated to actually pass these two fields through (previously would have silently dropped any field not in its explicit whitelist — a real bug found and fixed this session, see `KNOWN_ISSUES_DAY93.md`).

---

## Unchanged, for reference

No other endpoint shapes changed this session. `/api/cycles` and `/api/econ`'s response *shapes* are identical to Day 92 — only internal text (`Seasonal Regime` card's `phase`/`history` strings) and internal composite-selection logic (`_build_composite()`'s PMI lookup) changed, neither of which alters the JSON contract's fields or types.
