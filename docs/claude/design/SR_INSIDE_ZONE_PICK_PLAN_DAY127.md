# S&R: the zone price is INSIDE must be the nearest support (Day 127) — PLAN v1
Found by the Statement Audit (TS1b "Buy == nearest support zone's edge") on the 117-ticker universe; first named by the phase-2 review as latent.

## Evidence (PLD, universe run 3, price 125.56, ATR 2.51)
Zones: A 122.60-124.69 (below price), B 125.38-127.82 (price is INSIDE it, `insideZone: true`). `nearest` is flagged on A, not B.
Cause: `simple_sr.compute_simple_sr.pick(side)` (backend/simple_sr.py ~195-200) sorts candidates by `abs(zone edge - price)`; for support the edge is the zone HIGH. B's high (127.82) is 2.26 away, A's high (124.69) is 0.87 away, so A wins.
But the module's own rule 3 says "support = the zone just below price (or the one price is inside it)" and the Day-126 comment "inside a zone -> it's the support (Fable #11)". Consequences on the page: Buy = `max(support)` = 127.82 (B's high, so "Buy $127.82 ... 1.8% above the last close"), while the Key Levels "Support" row and the shaded band follow the `nearest` flag (A: "$122.60 - $124.69 · 0.7% below"). Two different supports on one card.

## Change
In `pick(side)` rank an inside zone first: sort key = `(0 if z['insideZone'] else 1, abs(z['_edge'] - price))`. For resistance nothing changes (an inside zone is always classed as support, so `insideZone` is false for every resistance zone). The returned `support` list stays "nearest first", so its first element is the inside zone's high; `Buy = max(support)` is unchanged for every case where the inside zone is also the highest support edge (all current cases), and now equals the `nearest` zone's edge.
No change to zone building, merging, ATR, the window, `nearHigh52w`, or the frontend (PullbackPlan already has the "top of the support zone; price is inside it" wording keyed on `nearest && insideZone`).

## Tests
- `backend/test_simple_sr_inside_zone.py` (new): a planted frame reproducing PLD (two support zones, price inside the upper one, lower one's edge nearer): `nearest` on the inside zone, `support[0]` is its high; a case with price inside a zone and NO other zone; price between zones (no inside zone: unchanged, nearest by edge); inside a resistance-side situation unchanged; ties; one zone only.
- Audit: TS1b passes on PLD after the fix (re-dump PLD + AMD, META, QCOM). Full audit suites and page checker 55/55. Parity: confirm nothing else consumes `meta.zones[].nearest` differently (KeyLevels, PullbackPlan, keyLevels.js, checks A10).

## Questions for the review
1. Is "inside zone first" the right reading of rule 3 and the Fable #11 note, or should price-inside-zone be treated differently (e.g. when price is within the lower half)?
2. Who else consumes `support` order, `suggestedEntry`, `meta.zones[].nearest` or `insideZone` (grep backend incl. backtest, paper_trading, compare_sr_engines.py, sr_plan.py, and frontend) and does any rely on the old ordering?
3. Any case where the fix gives a worse Buy (a Buy far ABOVE price because the inside zone is wide)? Should the Buy for an inside zone be the zone high, the price, or the zone low?
4. Test gaps.
