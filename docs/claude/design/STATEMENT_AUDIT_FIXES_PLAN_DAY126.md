# Statement Audit fixes (Day 126) — PLAN v1

Source: `docs/test/Statement_Audit_20261117/REPORT.md` and the Known Issues entries added the same day. Five findings; #5 (stale docstring) is already fixed.
Honest scope: after these fixes the TECHNICAL READ card is clean on the 7 audited tickers. Other cards (Trade Setup, Breakout, S&R levels, MR Read, Price Data,
Relative Strength, Fundamentals, Market backdrop, Data Sources, earnings/sector badges) are NOT YET COVERED; "good" only holds for what was audited.

## 1. Zero-volume funds print meaningless volume numbers (HIGH, SOXL.NE)
Cause: `TechnicalRead.jsx:226` `effRvol = barComplete ? meta.rvol : (prevBar?.rvol ?? meta.rvol)`: when the prior bar's RVOL is None (average volume 0) it
falls back to TODAY's partial-bar `meta.rvol` (backend: today's tiny volume / an average that includes only that volume = 50.0) and labels it "Last session (prior date)".
Also `meta.obv.trend` is computed from a zero-volume history plus today's partial volume ("falling"), and feeds the volume tally.
Fix:
- Backend `/api/sr` (backend.py ~1893-1910): `volume_available = completed bars' volume over the last 50 bars sums to > 0`. When false: `meta.volumeAvailable = false`,
  `meta.rvol = None`, `meta.obv = None` (calculate_obv is not called), `prevBar.rvol = None`. When true nothing changes; add `meta.volumeAvailable = true`.
- Frontend: remove the `?? meta.rvol` fallback (a missing prior-bar value is "unavailable", never today's number under a past date). `deriveEntryVolume` returns
  `{state:'unavailable', reason:'no volume data for this fund'}` when `meta.volumeAvailable === false`; the card shows one plain line ("Volume isn't reported for this fund, so the
  volume reads are left out.") and hides the bars, tally and "Volume detail". Callers of `meta.rvol`/`meta.obv` elsewhere must tolerate null (grep, Golden Rule 54): App DIST badge
  (`obv.trend`), breakout panel, Scan, MR, watchlist code in the backend.

## 2. Dividend-adjusted "1-year high" disagrees with the Price Data card (MEDIUM, F)
Decision (recommended, smallest safe): LABEL, do not change the price basis. The 8 trend criteria, SMAs and the 25% rule stay on the engine's adjusted bars (changing basis moves
Trend Template scores for every dividend payer and is its own plan). In `deriveTrendChecks` the 1-year-high row detail adds, only when the Yahoo 52-week high
(`stock.fiftyTwoWeekHigh`, the Price Data card's number) differs from the engine's high by more than 0.5%: "... below the $17.38 high (dividend-adjusted; Yahoo's 52-week high is $17.78)".
No verdict, just both numbers and why. `deriveTrendChecks` gets a third optional arg `rawHigh`. Audit T9x then expects the explanation instead of a bare mismatch.

## 3. ADX counts today's unfinished bar (LOW, up to 1.1 points mid-session)
Make `/api/sr` compute `meta.adx` on completed bars (`drop_forming_bar` on the frame used for ADX only; candle, RVOL, currentPrice and levels unchanged). Consumers of `meta.adx`:
`App.jsx:443` (verdict input via determineVerdict / categoricalAssessment.js:577,840), `KeyLevels.jsx`, `keyLevels.js:119`, Technical Read. This IS a verdict input, so: grep the Python
categorical engine and watchlist for ADX use (Golden Rule 59 parity), state the size (0.5-1.1 points, mid-session only, same family as the Day 126 forming-bar fix), and confirm the
86,400-case parity grid is unaffected (ADX is a grid INPUT). If any parity/threshold case sits on the 20 line, report it.

## 4. Display rounding at the 0.25 / 0.75 close-location thresholds (LOW)
`meta.candle.closeLocation` and `prevBar.closeLocation` are rounded to 2 decimals before `volumeThresholds` compares to 0.25 / 0.75 (AAPL 0.2526 -> 0.25 -> "near the day's low").
Return 4 decimals (backend.py:1921, 1963). Check every consumer and test that expects 2 decimals (volumeThresholds, TechnicalRead, tests, KeyLevels, watchlist).

## 5. Tests and audit updates
- `backend/test_sr_volume_unavailable.py`: zero-volume frame -> `volumeAvailable false`, rvol/obv None; normal frame unchanged; 4-decimal closeLocation; ADX on completed bars when the last bar is forming (frozen clock + fake provider as in `test_forming_bar_routes.py`).
- `frontend/scripts/test_entry_timing.mjs`: unavailable state, no `?? meta.rvol` fallback (prevBar.rvol None + partial meta.rvol 50 must give no RVOL), `deriveTrendChecks` adjusted-high label shown/not shown, boundary at 0.5%.
- `audit_statements.py`: Z1 passes when the card says volume is not reported; T9x passes when the explanation is present; T4 passes on completed-bar ADX; V1/V3 borderline resolve to PASS; U1 exemptions for the new sentences. Re-run all 7 dumps: expect 0 WRONG, 0 HIGH MISLEADING.
- Page checker 44/44 and every frontend/backend suite; screenshots of SOXL.NE and F Technical Read.

## 6. Risks for the review
1. `meta.obv = None` and `meta.rvol = None` reaching consumers that assume numbers (App DIST badge, breakout, Scan, MR, watchlist, paper-trading frozen code).
2. Verdict-input change from ADX (Golden Rule 59): is it acceptable and fully tested, or should the card alone show the completed-bar ADX?
3. Zero-volume detection rule: all-zero over 50 bars vs "mostly zero" (thin funds with some zero days); partial zeros must still show numbers.
4. The label rule for the adjusted high (threshold 0.5%, which source is "raw"), and whether the same adjusted/raw mismatch exists for the SMAs and 52-week LOW.
5. SOXL.NE-specific: the Canadian NEO fund may get volume from another source later; the rule must be data-driven, not ticker-based.
6. 4-decimal closeLocation: any place printing it.

## 7. Process
Plan -> Opus review -> build -> final three passes -> re-run the Statement Audit -> Known Issues (move the 4 entries to Changes) -> ledger -> commit.
