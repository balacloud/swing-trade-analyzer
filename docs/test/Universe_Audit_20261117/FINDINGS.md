# Universe run (117 tickers, Analyze tab) — findings so far (Day 126, partial; not yet fixed)
Run: 117 tickers loaded cleanly. Audits: Technical Read 4032 PASS / 68 WRONG / 26 MISLEADING; cards 3996 / 58 / 38; backdrop-fundamentals-MR 3543 / 51 / 17. Reports: REPORT.md, REPORT_CARDS.md, REPORT_CARDS2.md. Dumps are local only (dump_*.json).
## Root cause 1 (most WRONG rows): different cards read different price histories on one page
Clusters on dividend payers (DUK, SO, PG, CVX, COP, JNJ, LIN, CAT, GE, NEE, AAPU...): T6/T7/T8/T9 (patterns vs stock), BO1/BO2/BO5 (breakout), MR-sma, RS-toggle.
Evidence (CAT, same page load): /api/stock 52-week high 1073.46 and 200-day mean 807.00, /api/patterns high 1068.93 and 803.95 (0.4%, dividend-sized).
Probable causes: (a) cache_manager.py:269 `_period_to_min_rows('2y')` = 504 but Yahoo returns 501 rows, so the OHLCV cache is treated as a miss on EVERY call and each route refetches ("cache has 501 rows, need 504+"), (b) provider alternation: Twelve Data (breaker flapping, probably unadjusted for dividends) vs Yahoo (dividend-adjusted). Verify with providers/twelvedata_provider.py params (no `adjust`).
Proposed fix (needs plan + Opus review): realistic row threshold (about 95% of 504), and one dividend-adjustment basis across providers; re-run the universe.
## Other clusters to triage
- RS1 "not found" on 9 young/short-history funds (AVGC, COPZ, DRAL, DRAM, SPCL...): RS card missing or different text when history is short.
- FU5 21x "Can't check" for Fundamentals on stocks/Canadian names (provider returned nothing?) vs audit expecting flags.
- MR-row-volume 8x on thin Canadian ETFs (CARS.TO...): "$26,790 traded" shown while audit expects "no volume data".
- V6/V7/V5 volume ratios differ on a few names; T4 ADX mismatch on 5; TS1b (Buy vs nearest zone) fires on AMD, META, QCOM (the latent Medium bug is real); L-note/T5/HB4 last-close mismatch on AMD.TO, BRKU, VFV.TO (stale date Nov 13 vs Nov 16).
- CAT is NOT a split: it genuinely fell 1073 -> 570 in this data.
