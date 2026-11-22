
# ══════════════════════════════════════════════════════════════════════════════
# CONTEXT TAB — COMPLETE SPECIFICATION v1.0
# Swing Trade Analyzer v4.18
# Date: February 25, 2026
# ══════════════════════════════════════════════════════════════════════════════

## 1. PURPOSE
One unified tab that answers: "Is the macro environment right to act on my signal?"
Human is always the final decision-maker. This tab is PRE-FLIGHT CONTEXT ONLY.

## 2. LAYOUT STRUCTURE

### Navigation Bar (top)
- App title left: "📊 Swing Trade Analyzer v4.18"
- Tabs: Analyze | Scan | Options | [Context ACTIVE] | Validation | Data Sources
- Ticker search pill top-left: shows "🔍 AMD · $178.42 ▲+9.1%"
- Active tab highlighted: blue border + blue text

### Overall Regime Banner (below nav, full width)
- Background: green/yellow/red tint based on overall score
- Shows: "🌍 OVERALL MACRO REGIME: 🟢 FAVORABLE"
- Shows: "7 of 10 indicators supportive · 2 neutral · 1 adverse"
- Progress bar: left-to-right fill (green), width = % favorable
- Right side: timestamp + data sources

### Three-Column Layout (main content)
Columns A | B | C — equal width 33.3% each

---

## 3. COLUMN A — CALENDAR & YIELD CYCLES
Header: "📅 Calendar & Yield Cycles"
Subtext: "Global · cached 6h · no ticker needed"
Badge: "🟢 4 · 🟡 1 · 🔴 1"

### 6 Cycle Cards (each card shows):
Line 1: Icon + Name (bold, white)
Line 2: Current value + phase signal (gray)
Line 3: Data source + FRED series ID (darker gray)
Line 4: 📊 Historical base rate (blue, smallest)
Right badge: 🟢/🟡/🔴 FAVORABLE/NEUTRAL/ADVERSE

#### The 6 Cards:
1. 📈 Yield Curve
   - Value: +0.62% Normal · Steepening ↑
   - Source: FRED T10Y2Y
   - History: Avg S&P +13.2%/yr in this regime
   - Regime: 🟢 FAVORABLE

2. 🏭 Business Cycle
   - Value: INDPRO 103.2 · +0.3% MoM · Plateau
   - Source: FRED INDPRO proxy
   - History: PMI proxy — watch for <50
   - Regime: 🟡 NEUTRAL

3. 🏛️ Presidential Year
   - Value: Year 2 of 4, Q1
   - Source: Calendar computed
   - History: Weakest year — avg +3.33%/yr
   - Regime: 🔴 ADVERSE

4. 📅 Seasonal Regime
   - Value: Strong Season (Nov–Apr) · Feb
   - Source: Computed — 65 days to May 1
   - History: Best 6mo historically
   - Regime: 🟢 FAVORABLE

5. 🏦 FOMC Proximity
   - Value: Next: Mar 18 · 21 days away
   - Source: Hardcoded FOMC dates
   - History: Ideal: 15–40 days from FOMC
   - Regime: 🟢 FAVORABLE

6. ⚡ Quad Witching
   - Value: Next: Mar 20 · 23 days away
   - Source: Computed (3rd Fri Mar/Jun/Sep/Dec)
   - History: No pin risk on current positions
   - Regime: 🟢 FAVORABLE

### Bottom summary box (Column A):
"7/10 indicators favorable · Presidential Yr2 only headwind"
"FOMC 21d · Quad Witching 23d · No options blocks active"
"Normal cycle position sizing justified"

---

## 4. COLUMN B — ECONOMIC INDICATORS
Header: "📊 Economic Indicators"
Subtext: "FRED API · Monthly/quarterly · cached 6h"
Badge: "🟢 3 · 🟡 1 · 🔴 0"

### 4 Economic Indicator Cards (same card format as Column A):

1. 💵 Fed Funds Rate
   - Value: 5.25–5.50% · Hold (Cutting bias)
   - Source: FRED FEDFUNDS
   - History: Cutting w/o recession = avg +18% Yr1
   - Regime: 🟢 FAVORABLE

2. 📈 CPI Inflation
   - Value: 2.8% YoY · Core: 3.1%
   - Source: FRED CPIAUCSL · CPILFESL
   - History: Sweet spot 2–3%: avg S&P +15.6%/yr
   - Regime: 🟢 FAVORABLE

3. 🏭 ISM PMI
   - Value: 52.3 · Expanding
   - Source: ISM / FRED MANEMP proxy
   - History: PMI 50–55 = avg 1yr forward +10.1%
   - Regime: 🟢 FAVORABLE

4. 👷 Unemployment
   - Value: 4.1% · Stable (flat trend)
   - Source: FRED UNRATE
   - History: Rising trend = late cycle warning
   - Regime: 🟡 NEUTRAL

### Historical Regime Composite Box:
Title: "📖 Current Regime (Feb 2026):"
Content:
  "Fed Cutting + CPI 2.8% + PMI 52"
  "= Rising Growth + Falling CPI"
  "Historically BEST macro combo"
  "Avg S&P forward 12m: +18–22%"
  "Source: S&P Global 50yr factor study"
Border: blue

### Options Block Status Box:
"⚙️ Options Block Status"
"FOMC 21d · Quad Witching 23d"
Badge: "✅ NO ACTIVE OPTIONS BLOCKS" (green)
→ If FOMC < 5 days OR Quad Witching < 3 days:
  Badge changes to: "⛔ OPTIONS BLOCK ACTIVE" (red)

### Bottom summary box (Column B):
"CPI 2.8% sweet spot · PMI 52 expanding"
"Fed easing bias · Unemployment stable"
"BEST historical macro combo — Rising growth + Falling CPI"

---

## 5. COLUMN C — NEWS SENTIMENT + SHORT INTEREST
Header: "📰 News Sentiment — [TICKER]"
Subtext: "Per-ticker · Alpha Vantage NEWS_SENTIMENT · cached 4h"
Badge: overall sentiment badge (🟢 BULLISH / 🟡 NEUTRAL / 🔴 BEARISH)

### Signal Alerts (2 rows):
Row 1: News signal (green/yellow/red bg)
  "🟢 Strong bullish news flow · 3 bullish · 0 bearish · 1 neutral"
Row 2: Short interest signal (yellow/red bg)
  "📊 Short Interest: 8.1% float · Normal · 2.3 days to cover"

### Sector + Peer Row:
"Sector: Technology    Peers: [NVDA] [INTC] [QCOM]"
Peers = clickable chips (blue), click loads peer's news

### Article Feed (5 articles):
Each article row:
  - Emoji (🟢/🟡/🔴) by score
  - Title (truncated to 55 chars, clickable blue link)
  - Source · Date · relevance score
  - Sentiment score badge (+0.34, -0.09 etc)

### Conflict Check Banner:
Green: "✅ No Conflicts Detected — Cycles FAVORABLE · News BULLISH"
Red:   "⚠️ CONFLICT — Adverse cycles + Bearish news · Reduce size"
Orange:"🟠 PARTIAL CONFLICT — Mixed signals · Proceed cautiously"

### Macro Context Verdict (bottom of Column C):
"🎯 Macro Context Verdict — [TICKER]"
"Favorable cycles + Bullish news + No options blocks"
"Historical base rate this combo: avg +18–22% fwd 12m"
"⚠️ You are the final decision-maker. This is context, not advice."

---

## 6. REACT COMPONENT LOAD LOGIC

```
useEffect(() => { fetchCycles(); fetchEcon(); }, []);       // Columns A+B: once on mount
useEffect(() => { if (ticker) fetchNews(ticker); }, [ticker]); // Column C: per ticker
```

---

## 7. BACKEND ENDPOINTS

| Endpoint              | Returns                        | Cache  | Trigger         |
|-----------------------|--------------------------------|--------|-----------------|
| GET /api/cycles       | 6 calendar/yield cycle cards   | 6h     | App mount       |
| GET /api/econ         | 4 economic indicator cards     | 6h     | App mount       |
| GET /api/news/<ticker>| News sentiment + short interest| 4h/tkr | Ticker search   |
| GET /api/context/<t>  | All 3 combined in one call     | mixed  | Context tab open|

---

## 8. FRED API SERIES IDs

| Indicator        | Series ID  | Frequency |
|------------------|------------|-----------|
| Yield Curve      | T10Y2Y     | Daily     |
| Business Cycle   | INDPRO     | Monthly   |
| Fed Funds Rate   | FEDFUNDS   | Monthly   |
| CPI Headline     | CPIAUCSL   | Monthly   |
| Core CPI         | CPILFESL   | Monthly   |
| Unemployment     | UNRATE     | Monthly   |
| Consumer Sent.   | UMCSENT    | Monthly   |
| PMI proxy        | MANEMP     | Monthly   |

Base URL: https://api.stlouisfed.org/fred/series/observations
Free API key: fred.stlouisfed.org/docs/api/api_key.html

---

## 9. REGIME THRESHOLDS

### Yield Curve (T10Y2Y)
>= 0.5%   → FAVORABLE (Normal steepening)
0 to 0.5% → NEUTRAL   (Flat)
< 0%      → ADVERSE   (Inverted — recession risk)

### CPI (CPIAUCSL YoY)
<= 3.0%   → FAVORABLE (Sweet spot)
3.0–5.0%  → NEUTRAL
> 5.0%    → ADVERSE

### Fed Funds Direction
Cutting or hold w/ cutting bias → FAVORABLE
Hold neutral                    → NEUTRAL
Hiking                          → ADVERSE

### PMI (or proxy)
>= 52     → FAVORABLE
48–52     → NEUTRAL
< 48      → ADVERSE

### Unemployment (UNRATE)
< 4.5% AND flat/falling trend → FAVORABLE
4.5–5.5% OR slowly rising    → NEUTRAL
> 5.5% OR rapidly rising     → ADVERSE

### FOMC Proximity (days to next)
15–40 days → FAVORABLE
5–14 days  → NEUTRAL
< 5 days   → ADVERSE (options block)

### Quad Witching (days to next)
> 5 days  → FAVORABLE
3–5 days  → NEUTRAL
< 3 days  → ADVERSE (options block)

### Presidential Cycle
Year 1: NEUTRAL  (avg +6.5%/yr)
Year 2: ADVERSE  (avg +3.33%/yr, weakest)
Year 3: FAVORABLE (avg +19.8%/yr, strongest)
Year 4: FAVORABLE (avg +7.5%/yr, election boost)

### Seasonal
Nov–Apr → FAVORABLE ("Best 6 months" historically)
May–Oct → NEUTRAL   ("Sell in May" historically weaker)

---

## 10. OVERALL REGIME LOGIC

favorable_count = sum of all GREEN indicators
neutral_count   = sum of all YELLOW indicators
adverse_count   = sum of all RED indicators

if adverse_count >= 4:                         overall = ADVERSE
elif adverse_count >= 2 or favorable_count < 5: overall = NEUTRAL
else:                                           overall = FAVORABLE

progress_bar_pct = favorable_count / total_indicators * 100

---

## 11. HOW CONTEXT TAB FEEDS BACK INTO MAIN SYSTEM

| Context Signal            | Effect on Analyze Tab              |
|---------------------------|------------------------------------|
| overall_regime = ADVERSE  | Cap all BUY → HOLD (same as bear)  |
| CPI > 5%                  | Add ⚠️ "Valuation Headwind" badge  |
| PMI < 48                  | Shift sector hint → defensives     |
| has_options_block = True  | Block ALL options strategies       |
| news bearish + cycles adv | Show "⚠️ CONFLICT" red banner      |
| news bullish + favorable  | Show "✅ Context Aligned" green    |

---

## 12. FILES TO CREATE/MODIFY

NEW FILES:
  backend/cycles_engine.py      (Column A logic)
  backend/econ_engine.py        (Column B logic)
  backend/news_engine.py        (Column C logic — already specced)
  frontend/src/components/ContextTab.jsx
  frontend/src/components/CycleCard.jsx
  frontend/src/components/EconCard.jsx
  frontend/src/components/ArticleRow.jsx
  frontend/src/components/RegimeBanner.jsx
  frontend/src/components/ConflictCheck.jsx

MODIFY:
  backend/backend.py            (add 3 new endpoints)
  backend/cachemanager.py       (add cycles_cache, econ_cache, news_cache tables)
  frontend/src/App.jsx          (add Context tab + pass ticker prop)
  frontend/src/utils/categoricalAssessment.js  (read overall_regime for RiskMacro v2)

---

## 13. .env KEYS REQUIRED

FRED_API_KEY=your_key_here
# Get free at: fred.stlouisfed.org/docs/api/api_key.html
# No credit card. Instant. 1000 req/day free.

ALPHA_VANTAGE_API_KEY=your_key_here
# Already in .env if using existing features
# Get free at: alphavantage.co — 25 req/day free tier

---

## 14. BUILD ORDER (4 Days)

DAY 1 — Backend Engines
  □ Get FRED API key (5 min, free)
  □ Create cycles_engine.py — fetch T10Y2Y, INDPRO, compute presidential/seasonal/FOMC/QW
  □ Create econ_engine.py — fetch FEDFUNDS, CPIAUCSL, CPILFESL, UNRATE, MANEMP
  □ Create news_engine.py — Alpha Vantage NEWS_SENTIMENT + yfinance short interest
  □ Add tables to cachemanager.py: cycles_cache, econ_cache, news_cache
  □ Add /api/cycles, /api/econ, /api/news/<ticker>, /api/context/<ticker>
  □ Test: curl localhost:5001/api/cycles
  □ Test: curl localhost:5001/api/econ
  □ Test: curl localhost:5001/api/news/AMD

DAY 2 — React Components
  □ Create CycleCard.jsx (collapsible, colored border, history footnote)
  □ Create EconCard.jsx (same format as CycleCard)
  □ Create ArticleRow.jsx (emoji, title link, source, score badge)
  □ Create RegimeBanner.jsx (full-width, progress bar, summary counts)
  □ Create ConflictCheck.jsx (green/orange/red based on combo)
  □ Create ContextTab.jsx (assembles all components, 3-col layout)

DAY 3 — App Integration
  □ Add 'Context' to TABS array in App.jsx
  □ Wire currentTicker state as prop to ContextTab
  □ Feed overall_regime → categoricalAssessment.js (RiskMacro v2)
  □ Feed has_options_block → options_engine.py universal disqualifiers
  □ Add "Context" badge on Analyze tab when risk_flags present

DAY 4 — Testing
  □ Test: AMD (should show FAVORABLE + BULLISH news)
  □ Test: WMT (no news → graceful empty state)
  □ Test: Ticker with earnings in 3 days (options block fires)
  □ Test: cycle same ticker twice (second load = from_cache: True)
  □ Test: set CPI threshold to ADVERSE manually, verify RiskMacro changes
