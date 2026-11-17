# Statement Audit, phase 2: the cards that drive a trade (Day 126) — PLAN v1

Phase 1 (done): Technical Read + gauge/ladder + header price lines. First run found 5 WRONG / 8 MISLEADING, all fixed; re-run 266 PASS.
Phase 2 adds, in this order, the cards a trade decision leans on: **Trade Setup (pullback plan + key levels)**, **Breakout**, **Price Data**, **Relative Strength**,
then the **header badges** (earnings, sector, classification). Same protocol (MASTER_AUDIT_FRAMEWORK Part 7: checks S1-S5, verdicts PASS/WRONG/MISLEADING/UNVERIFIED,
every number token claimed or listed). Phase 3 later: Fundamentals, Market backdrop, Data Sources, MR Read, then the other tabs. Nothing is called covered that is not.

## 1. What the page says on these cards (from the code) and how each is checked
### Trade Setup: PullbackPlan.jsx + KeyLevels.jsx
| Statement | Source (S1) | S2 recompute / S3 words |
|---|---|---|
| Buy = top of the nearest support zone | `/api/sr` `levels` / `meta.zones` (backend simple_sr) | structural: support < last close (or inside zone), nearest by distance among supports, zone top >= bottom; the level lies inside prices the stock actually traded (some bar's [low, high] touches it); UNVERIFIED for "is this the right pivot" (engine definition, see §3) |
| "support, 3.3% below the last close" | arithmetic on buy and `srData.currentPrice` | (buy - close)/close from the bars; words "below/above"; "last close" must be the last COMPLETED bar, but `srData.currentPrice` is today's live bar mid-session (known Low): check which one the sentence uses |
| Stop = 2 ATR below the buy ("2 ATR below", "-x% from the buy", "floored at $0.01") | `meta.atr` = Wilder ATR14 | ATR from bars (audit_ref.wilder_atr), stop = buy - 2 x ATR, floor 0.01, % = (stop - buy)/buy |
| Target = bottom of the nearest resistance zone, "+z% from the buy" | `levels` | resistance > close, nearest, % arithmetic; "no resistance within 30% above" vs the proximity filter in the payload; "at its 52-week high" vs `nearHigh52w` recomputed from 252-bar high |
| "N : 1 reward : risk", "Risk $a to make $b a share" | `calculateRiskReward` | (target - buy)/(buy - stop), risk = buy - stop, reward = target - buy |
| "Size this plan" passes buy and stop | App.jsx `autoFillPositionCalculator` | the numbers handed to the calculator equal the plan's buy and stop (2 dp) |
| Key levels rows: "Support $a - $b · x% below · turned here N×" | `meta.zones` | zone bounds, % arithmetic; "turned here N×" = pivot touches: recomputed only if the engine's counting rule can be restated simply (§3), else UNVERIFIED |
| Key levels one-line price state (trend template, ADX, ATR) | `keyLevels.js` | words vs the numbers they quote (ADX < 15 "choppy" etc., with the completed-bar ADX now in `/api/sr`) |
| Rule-of-thumb text "2x", "7-8%" | copy | exempt list, reviewed |

### Breakout card (`/api/breakout/<ticker>`, breakout_detection.py)
Statements: "60-day high $X (measured before the last 10 days)", "close x% above/below", "broke out <date> on N.NN x normal volume", "<date> close", the status badge and `humanAction`, the copy "volume 1.5x normal or more, no more than 5% above".
Recompute: 60-day high = max over the 60 bars ending 10 bars before the last (rule restated from the module's constants), pct = (close/level - 1), RVOL = volume / mean of the prior 50 bars (VOLUME_BARS/MIN_VOLUME_BARS shared), status from those numbers; words "close"/"60-day" vs windows; the badge vs the numbers it summarises.

### Price Data card and Relative Strength card (App.jsx ~1100-1170; no `card-*` testid today)
Add `data-testid="card-price-data"` and `card-relative-strength` (markup only) so the dump can scan them. Statements: Current Price, 52-Week High/Low and "% from high" (now one source, Day 126), average volume, RS 52-week and 13-week and blended (rsCalculator.js growth-factor formula), "Stock / S&P 52W Return", market-cap-style numbers. Recompute RS from the stock and SPY bars; S5: Current Price vs header vs Technical Read vs plan; 52-week high equals the Technical Read's 1-year high.

### Header badges
Earnings "in N days" (calendar days, `calendar_days_until`), sector quadrant/RS/Mom/Rank "n/11", classification line, freshness dots ("Xm ago"). S2 where the inputs are in the payload (days = date - today), S3 words (calendar vs trading days), UNVERIFIED where the source is only a provider field.

## 2. Build
- `frontend/scripts/dump_page_statements.js`: also capture `/api/breakout/<t>`, `/api/earnings/<t>`, sector payloads; text per card (trade-setup, breakout, price-data, relative-strength, stock-header) with details opened; per-card `tokens`.
- `backend/audit_statements.py` split into per-card modules (`audit_cards/technical_read.py` existing logic moved unchanged, `trade_setup.py`, `breakout.py`, `price_data.py`, `relative_strength.py`, `header.py`) sharing the Row/verdict/claim/unclaimed machinery (`audit_core.py`). Phase-1 behaviour must be byte-for-byte unchanged (regression: the Phase-1 report's PASS count is the same).
- `audit_ref.py`: add RS growth-factor, 60-day-high rule, zone touch helpers. `test_audit_statements.py`: planted wrong number / wrong word / unclaimed number per new card, and the structural invariants (a support above the price must FAIL; a stop not 2 ATR below must FAIL).
- Report: one REPORT.md with a Coverage table (card, statements registered, tokens claimed, tokens unverified) so "what is covered" is read off, not assumed. Ledger row per card.
- Tickers: the Phase-1 seven plus one at a 52-week high (no resistance) and one with no support below, so those empty states are exercised.

## 3. Hard questions for the review
1. Support/resistance recompute: can `simple_sr`'s zones and "turned here N×" be restated in a short independent reference, or is "levels valid, arithmetic exact, engine rule UNVERIFIED" the honest ceiling? (Golden Rule 59: a second copy of an engine rule is its own drift risk.)
2. Is checking `srData.currentPrice` (live bar) vs the plan's "last close" wording a finding now or a known Low?
3. Missing statements on these cards I did not list (grep the real JSX): tooltips, `title`s, aria, nested details, KeyLevels text, App.jsx 1100-1170.
4. Per-card module split vs one file: risk to Phase 1.
5. Anything that would let a wrong number pass (tolerances, regex fragility, copy changes).

## 4. Process
Plan -> Opus review -> build -> run on the 9 tickers -> fix findings (each with its own tests) or log -> three passes -> Known Issues, ledger, framework history -> commit.

## 5. Review result (v2) — Opus: GO WITH CHANGES, applied
1. **Statement inventory corrected.** RS card shows "RS vs S&P 500" (rs52Week), "Stock 52W Return", "S&P 52W Return", "RS Rating (scaled, not a percentile)", the interpretation sentence (+ "(momentum accelerating/fading)" from the 13-week vs 52-week RS) and the absolute-momentum line; it shows NO 13-week or blended RS. Price Data shows Current Price, 52-Week High/Low, % from High, "Liquidity (Daily $)" (Yahoo avgVolume x price). The collapsed "Price & RS" toggle must be clicked open; add testids `card-price-data`, `card-relative-strength`.
2. **Finding now:** Trade Setup says "last close" but reads `srData.currentPrice` (today's live bar mid-session; differs from the completed close for 5 of 7 phase-1 tickers). Fix the input in PullbackPlan (last completed close = `prevBar.close` while forming) + S5 header-vs-plan row.
3. **Finding now:** Price Data "Liquidity" uses Yahoo avgVolume while the Technical Read says SOXL.NE has no volume (two volume sources). Fix: show "n/a, no volume data" when `meta.volume.available === false`; log the mixed source.
4. **Latent:** Buy = max(support) can disagree with the `nearest` flagged zone (inside-zone + width-cap split). Planted-fixture audit test + per-ticker S5 row "Buy == nearest support's edge"; engine fix logged (no ticker hits it).
5. **Wording overstates** ("at its 52-week high" when only within 3%; "None within 30%" while a recent unconfirmed high exists): fix copy to "near" / "no confirmed resistance".
6. **Verdict words** on cards (rsCalculator interpretation, keyLevels "strong/weak trend", "Compression", earnings title "HIGH RISK... Consider waiting", stale "does not affect the verdict"): logged as findings; fix the clearly stale/false ones.
7. Breakout "broke out <date>" moves daily for a steady climber; "Retest holding" fires on any undercut; "x normal volume" has two definitions on one page: logged, planted-series tests.
8. "Current Price" = last completed close (header shows live "Now"): wording row. 9. Short-history RS windows differ (stock iloc[0] vs SPY 252): row + log. 10. Money leftovers: `formatZoneRange` toFixed/no commas; "Size this plan" `toFixed` vs half-up: fix + planted tie test.
- **S&R recompute is feasible** (loop-based reference from the docstring, 5-bar swings, merge rule) with structural invariants; borderline merge decisions are UNVERIFIED-borderline, not WRONG. `meta.lastBarDate` / `barsUsed` exposed so the audit can assert the same last bar.
- **Design change vs the review:** new cards go in NEW modules that import the phase-1 machinery; `audit_statements.py` is not moved (no regression risk). Regression gate: the frozen phase-1 dumps are copied to `docs/test/Statement_Audit_phase1_frozen/` and every Technical Read row (id, shown, expected, verdict) must be identical before/after.
- Per-card "expected statements" lists keyed on payload state, so a missing statement is a finding, not silence; a card absent while its payload exists is WRONG; coverage table split into recomputed / arithmetic-only / structural / UNVERIFIED / not reached.

## 6. Result (Day 126)
Built per §5. Final run on 7 tickers: phase 2 254 PASS / 0 WRONG, phase 1 264 PASS / 0 WRONG. Fixed in the app: plan "last close" input, "near its 52-week high (within 3%)", "Last close" label, liquidity N/A for zero volume,
numbers instead of verdict words (key-levels state, RS sentence, earnings tooltip), stale and false copy, breakout volume window wording, one money format in zone ranges / Size this plan / data attributes. Logged: Buy vs nearest
zone (Medium, latent), RS short-history windows, provider one-cent gaps, zone-reference borderline cases. Deviation from the review: new cards live in a new module (`audit_cards.py`) that imports phase 1 instead of moving it.
