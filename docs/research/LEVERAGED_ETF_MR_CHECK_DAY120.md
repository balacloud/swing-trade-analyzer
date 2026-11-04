# Reddit Swing-Trading Advice vs. STA, and an MR Check on SOXL / GDXU / DRAL — Day 120

> **Date:** 2026-11-02 (prices as of the 2026-10-30 close)
> **Type:** Discussion record and a one-day snapshot. Not a backtest, and not a change to STA.
> **Scope agreed with the user:** fundamentals, holding period, journaling, and how many rules must agree
> are the user's own calls. Claude checks for splits on these tickers and explains stops and sizing.

---

## 1. How well STA matches a Reddit swing-trading summary

| # | Reddit point | STA today | Aligned? |
|---|---|---|---|
| 1 | Trade with the trend | Trend Template / 200 SMA; MR only buys above the 200 SMA | ✅ |
| 2 | Wait for a pullback | Breakout Status (Retest / Building Base), MR scanner, Sectors pullback screener | ✅ |
| 3 | Support & resistance | S&R engine (nearest-level fix, Day 112) | ✅ |
| 4 | Consolidation → breakout | VCP / Cup & Handle / Flat Base, Price Structure card | ✅ |
| 5 | Simple indicators | RSI, MAs, RVOL all present (volume is shown, not part of the verdict) | ✅ |
| 6 | Entry / stop / target | Trade Setup card, ATR stops, R:R | ✅ |
| 7 | Risk first | 2% rule documented; Settings slider still allows 5% (open bug) | ⚠️ |
| 8 | One setup | STA runs several engines; picking one is the user's call | ⚠️ |
| 9 | Fundamentals for selection | Out of scope (user's call) | n/a |
| 10 | Patience + records | The user keeps their own journal | ✅ (user) |

**Disagreements recorded:**
- The Reddit flow (trend → pullback/breakout → volume → R:R) is close to STA's momentum Config C, which tested
  as PF 0.53 on 41 trades after the Day 112 S&R correction. Path B, the live version, was retired as a null.
  Good habits, not an edge by themselves.
- "Don't buy solely because RSI is low" is half right. Low RSI(2) on a liquid stock **in an uptrend** is MR
  (broad), STA's one confirmed edge (194+ trades, PF ~2.5). Low RSI with nothing else is the bad version.

## 2. Theory: why low RSI sometimes works

A sharp drop is either an **overreaction** (panic, forced selling: buyers return within days if the larger
trend is up) or **new information** (the market repricing; low RSI is the start of a move). RSI can't tell
them apart. The 200-day-average filter is a rough proxy: above it, an overreaction is more likely; far below
it, a repricing is more likely.

## 3. Stops, in plain terms

A stop has to sit farther away than a ticker's normal daily wiggle, or noise sells you out. STA's MR stop is
the tighter of 5% below entry or 1.5 × ATR below entry. That fits a stock moving 2–3% a day, but SOXL moves
~18% a day, so a 5% stop is less than a third of one normal day. A stop that fits SOXL is ~25% away, which
means a much smaller position for the same dollar risk: $200 of risk buys $4,000 of a 5%-stop stock but
only ~$800 of SOXL.

## 4. Split check

yfinance and IBKR (contract IDs: SOXL 73340487, GDXU 593821778, DRAL 895506712) agreed on prices for all
three: Oct month-end closes of 77.05 / 64.34 / 6.89 on yfinance vs 77.05 / 64.34 / 6.88 on IBKR. Neither
series has a split-sized jump in the past year. IBKR's 1-year `include_corporate_actions` returned no split
(only a SOXL cash dividend on 2026-09-22), even though Day 107 had recorded a 3-for-1 split on 2026-05-25
for GDXU/SOXL (Golden Rule 46). The prices are internally consistent either way. **Recheck splits every time
these tickers are used.**

DRAL = Defiance Daily Target 2X Long DRAM ETF (BATS), listed ~June 2026.

## 5. STA MR rules applied to the ETFs (`mean_reversion.detect_mr_signal`)

Rules: RSI(2) < 10, price > 200 SMA, price > $10, 20d dollar volume > $25M.

| Ticker | Close | 200 SMA | vs SMA | RSI(2) | ATR % of price | MR |
|---|---|---|---|---|---|---|
| SOXL | 77.05 | 124.25 | −38% | 10.8 | 17.8% | No (below 200 SMA) |
| GDXU | 64.34 | 184.55 | −65% | 8.2 | 15.9% | No: oversold but trend broken |
| DRAL | 6.89 | n/a | n/a | 19.6 | 12.9% | Can't run (90 bars) |

## 6. Same check on the underlyings (untested idea: judge a leveraged ETF by its underlying's trend)

| ETF | Underlying | vs 200 SMA | RSI(2) | Read |
|---|---|---|---|---|
| SOXL | SOXX | −1.0% | 11.6 | Right on the line |
| SOXL | SMH | +0.6% | 11.6 | Right on the line, close to an MR signal |
| GDXU | GDX | −14.9% | 8.4 | No: the underlying confirms the trend is broken |
| DRAL | DRAM (Roundhill Memory) | n/a (147 bars) | n/a | Can't run |
| DRAL | MU (stand-in only, not the index) | +18.5% | 20.4 | Not oversold |

**Takeaway:** for semis, 3x leverage makes SOXL look far worse than its sector, which sits right on its
trend line. For gold miners, the underlying agrees with GDXU that the trend is broken. One-day snapshot only.
