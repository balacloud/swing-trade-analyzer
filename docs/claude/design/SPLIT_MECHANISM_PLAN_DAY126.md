# Split mechanism: Plan v1 (Day 126)

**Status:** PLAN v2 (Opus review done: GO with 6 MUST, all adopted in §9, which overrides §2-§7 where they differ). Next: build, then three review passes.
**Why:** SOXL.NE (BetaPro, user's most-traded fund) split 3:1 on 2026-05-25 (Global X notice; our bars show 141.84 -> 47.24, x0.333). Yahoo AND EODHD both left the old prices unadjusted, so every indicator on SOXL.NE that looks back past that date is wrong (ATR, RSI, S&R, 52-week high). The Data Sources tab already flags it (WARN/FAIL); nothing fixes it. Leveraged funds split and consolidate often (the same Global X notice also lists consolidations such as HOD 1:25). **User (Day 126): "that stock splits check has to be done as a mechanism."**

## 1. What exists today
Detection only: `data_quality.jump_moves` (one-day close move over 40%) -> WARN. No adjustment anywhere. Tradier is split-adjusted for forward splits but wrong on reverse splits (QPUX x3.00, Golden Rule 46).

## 2. Design (four parts, one rule each)

### 2.1 Known-splits table (the only source of truth for adjusting)
`backend/reference/known_splits.json`: `[{symbol, date (first split-adjusted trading day), ratio (new shares per old share: 3.0 = 3-for-1, 0.04 = 1-for-25), source_url, verified_on, note}]`. Hand-curated, each row backed by an issuer notice. **STA never adjusts from a guess.** A wrong adjustment silently corrupts every indicator, which is worse than a visible warning.

### 2.2 One adjuster, applied once, idempotent
`backend/split_adjust.py`: `adjust_for_splits(df, symbol) -> (df, applied:[...])`. For each table row for the symbol: look at the bar on `date` vs the previous bar. **Apply only if the jump is actually present** (`close[date]/close[prev]` within 5% of `1/ratio`... i.e. a 3:1 split shows ~0.333): then divide open/high/low/close of every bar before `date` by `ratio` and multiply volume by `ratio`. If no jump is present the provider already adjusted: do nothing (this prevents double adjustment, and makes the table safe when a provider fixes its data later). Returns what it did so the tab can say it.
Applied at the single point where OHLCV frames leave the cache/provider layer for the app (to be located in Phase A by caller grep, Golden Rule 54), so `/api/stock`, `/api/sr`, MR, scan all see adjusted bars. The stored cache stays raw (so the audit still sees the provider's real data).

### 2.3 Detector: tell the user about splits the table does not know
In `data_quality.check_history`: a jump in the last 260 bars whose size matches a split signature (ratio within 3% of 1/k or k, k = 2..50, also 1/25-style) and is **not covered by the table** -> **FAIL** "looks like an unadjusted k:1 split on <date>, not in known_splits.json" (was WARN). A big jump that matches no signature stays WARN ("real move or split"). A jump covered by the table is shown as PASS with "split-adjusted by STA, 3:1 on 2026-05-25".

### 2.4 Sweep (finds the unknowns once, then it is a standing check)
`backend/backtest/audit_splits.py`: for every instrument in the identified master list (80) fetch from cache, list every jump over 40% in the full stored history, classify (matches signature / not), cross-check the table, and print what needs a source check. Results go to `docs/test/Splits_<date>/REPORT.md`. Each candidate is verified against an issuer/news source before it enters the table.
Standing check = the detector in 2.3 (runs for any ticker the user opens) plus a line in the audit script.

## 3. What does NOT change
No provider code, no cache contents, no backtest, no verdict logic. The only live-number change: SOXL.NE (and any ticker later added to the table) gets correct prices. Verdict parity and the golden indicator snapshot must stay bit-identical for the other 23 tickers; SOXL.NE changes (expected, shown).

## 4. Failure states
Table missing/unreadable -> adjust nothing, log once, the detector still FAILs unexplained splits (no silent pass). Malformed row -> skipped with a log line and shown in the tab. Split date not in the frame (history shorter) -> not applicable, no error. Two rows same date -> error shown. Provider adjusted only partly (jump ratio not near 1/ratio) -> do not adjust, FAIL "table says 3:1 but the jump is x0.5".

## 5. Tests
Unit: forward 3:1, reverse 1:25, jump absent (provider adjusted) -> no change, partial mismatch -> no change + flag, two splits in one history, split on the first/last bar, volume scaling, idempotence (adjust twice == once), ratio signature classifier (real 45% crash does not match). Integration: real SOXL.NE frame from the audit cache: 311 bars, close before 2026-05-25 divided by 3, ATR/RSI computed before/after. Golden snapshot: 23 tickers identical. Page checker A11: SOXL.NE shows the "split-adjusted" line.

## 6. UI (less to read)
One line in the existing quality block: "Split-adjusted by STA: 3-for-1 on May 25, 2026 (source: Global X notice)". Nothing else. SOXL.NE's known-FAIL in the page checker (`KNOWN_VERDICT`) is replaced by the new expected state.

## 7. Build phases
A. Caller graph for where frames leave the cache; the sweep over the 80 instruments (facts first). B. `split_adjust.py` + table (SOXL.NE row only, plus any sweep-verified rows) + tests. C. Wire at the single point; detector upgrade; tab line. D. Verify: suites, golden diff (only SOXL.NE moves), parity, page checker. E. Docs, Known Issues.

## 8. Questions for the reviewer
1. Where exactly do OHLCV frames leave the cache for the app, and are there paths that bypass that point (MR scanner, paper trading, `/api/sr`, scan, 4H/intraday, backtests)? Does adjusting at that point change anything that feeds a stored result?
2. Is "apply only when the jump is present" sound? Failure cases (jump on a different day than the table says by a day; market-holiday offsets; provider adjusted only some columns; Yahoo adjusting later while our cache is stale)?
3. Is the signature rule (within 3% of 1/k or k) safe from false FAILs on volatile 3x funds (real one-day moves of -33%)? Give a concrete rule and test the signature against the cached frames.
4. Does the cache-stays-raw design cause the audit/data-quality check to disagree with what the user sees?
5. Anything in the Day-126 data-quality design this duplicates or contradicts (Golden Rule 59)?
6. Decision-fatigue: is one tab line enough?

## 9. v2 changes after the Opus review (these override the sections above)
Verified in code before adopting: `cache_manager.py:269-274` hides frames under 504 rows (SOXL.NE has 311, so it is never served from cache); `orchestrator.get_ohlcv` has three exits (cache hit, fresh fetch, stale cache); the page's 52-week high/low are Yahoo `info` values (`backend.py:1153-1154`).

**MUST**
1. **Insertion point = the orchestrator, not the cache.** One helper `_deliver(ticker, df)` applied at all three exits of `DataProvider.get_ohlcv` (and in `get_intraday_ohlcv`, for the 4H RSI). Returns a COPY (callers rename columns in place), runs after `set_cached_ohlcv`, so the cache stays raw.
2. **Bypass list decided in writing.** Direct yfinance fallbacks in `backend.py` (:1067, :1237, :1745, :2082, :3783, :3853) and `breakout_routes.py:54`: route them through the same adjuster call. Bulk `yf.download` (sector rotation, RS ranking in `scan_queries.py`, `market_phase_engine.py:95`): accepted bypass (US symbols Yahoo adjusts). Backtests and the TradingView scan: out of scope. `/api/provenance` reads raw on purpose.
3. **52-week high/low:** for a symbol with an applied split, compute both from the adjusted frame in one place (not Yahoo `info`); otherwise unchanged. Live check of what Yahoo reports for SOXL.NE during the build.
4. **One classifier** in `split_adjust.py`, also called by `data_quality` (replaces the 5% and 3% tolerances). For table row (date D, ratio R) examine bars within +-2 of the first bar on/after D; s = close[i]/close[i-1]:
   - unadjusted: |ln(s*R)| <= ln 1.35 and |ln(s*R)| < |ln s|/2 -> adjust at that bar (say so if it is not D);
   - already adjusted: no bar with |ln s| >= |ln R|/2 -> do nothing;
   - adjusted the wrong way (QPUX on Tradier: x0.3129 vs 1/3): FAIL, do not adjust;
   - anything else: FAIL "ambiguous", do not adjust;
   - ratios within ln 1.5 of 1 (3:2, 4:3): exact bar and residual <= 10%.
5. **No silent skip.** D before the first bar -> not applicable; D after the last bar -> "pending" (flag if a live quote is mixed in); D inside the range -> the +-2 window, never silent. (2026-05-25 is US Memorial Day but trades in Canada; QPUX's Tradier step is 3/20 vs IBKR 3/23.)
6. **Correct expectations.** The golden indicator snapshot reads the audit cache directly, so it must be fully bit-identical (SOXL.NE included); SOXL.NE before/after is proved by a separate integration test on the cached frame. SOXL.NE's page-checker verdict stays **FAIL** (100% flat bars, zero volume: integrity), so the "split-adjusted" line is a separate A11 check, and the tab says ATR there is still a close-only approximation.

**SHOULD**
7. Audit scripts report raw and after-STA ("raw x3.02; after STA: matches") so `read_audit_summary` does not contradict the tab.
8. **Detector rule (measured):** flag "possible k:1 split" only if |ln(s*k)| <= ln 1.02 for whole k in 2..50 with k >= 3 (k = 2 only when volume confirms). Integer k only: no false positives on the 24 audit tickers + 74 cached frames (real moves seen: QPUX +47.6%, SPCL +56.6%, SOXL +54.8%, ^VIX +69.7%, none near an integer). Everything else stays WARN. This deliberately changes `quality_level`'s "jumps can only WARN" (`data_quality.py:137`) and `test_data_quality.py:64`: update both on purpose. Known gap: 40% cannot see 3:2 or 4:3 splits; only the table can.
9. Seed and cross-check the table with IBKR's saved split list (`data_audit_vs_ibkr_20261114.json`: SOXX 3:1 2026-11-05, QPUX 1:3 2026-03-23, GDXU.TO 3:1 2026-05-25, AMD.TO 7:1 2026-10-16, MU.TO 5:1 2026-03-10). Those providers already adjusted: they are the "no-op" fixtures. Only SOXL.NE is unadjusted.
10. Paper-trading ledger rows crossing a split (MNST -50.8% "stop_hit_gap", SOXX): logged as a Known Issue, not changed (program discontinued Day 113).
11. Sweep reads `read_ohlcv_entry` only (never `get_cached_ohlcv`, never a provider); the cache holds 74 frames, max 2 years; report which master symbols have no frame.
12. Tests added: QPUX-Tradier wrong-direction fixture, step one bar off, split on a holiday, pending split, ambiguous x0.516 day, adjuster returns a copy and leaves the raw cache untouched, no-op fixtures (GDXU.TO, SOXX, AMD.TO, MU.TO), table validation (ratio > 0 and != 1). UI: one line, shown only when something was adjusted or is wrong.

## 10. Review log
Opus, Day 126: GO with 6 MUST + 6 SHOULD/NICE, all adopted above. Wrong premises corrected: cache insertion point; 52-week fix; golden snapshot expectation; "known FAIL replaced"; the Tradier reverse-split description (it applied the split the wrong way, one bar early); 5%/3% tolerances; "80 instruments, full history".
