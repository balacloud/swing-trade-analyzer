# PROJECT STATUS - Day 28

> **Version:** 3.0
> **Date:** January 14, 2026
> **Focus:** Position Sizing System (Van Tharp Architecture)

---

## Day 27 COMPLETED

### Critical System Validation
- [x] **Backtest created:** `backtest_technical.py` - tested 75-point scoring system
- [x] **Results:** 310 trades, 49.7% win rate, 1.40 profit factor, 1.30% expectancy
- [x] **Key finding:** Higher scores did NOT correlate with better outcomes
- [x] **Hypothesis (55% win rate) REJECTED** - system is essentially random

### Research Completed
- [x] Van Tharp "Trade Your Way to Financial Freedom" - **90% of performance = position sizing**
- [x] Alexander Elder "Trading for a Living" - Triple Screen, 2%/6% rules
- [x] David Aronson "Evidence-Based Technical Analysis" - scientific method
- [x] Academic research: Momentum works (AQR, Fama-French)

### Simplified System Built
- [x] Created `simplifiedScoring.js` - 4 binary criteria (Trend, Momentum, Setup, R:R)
- [x] Created `backtest_simplified.py` - Results: 29 trades, 51.7% win rate, 1.43 profit factor
- [x] Added toggle in App.jsx between "Full Analysis" and "Simple Checklist" views

### Critical Discovery
**We optimized the WRONG thing:**
- Entry signals contribute ~10% to trading results
- Position sizing contributes ~90% to trading results
- Our 75-point system spent 27 days optimizing the 10%
- Missing: Position sizing, R-multiples, expectancy tracking, exit strategy

---

## Day 28 PRIORITIES

### Phase 1: Core Position Sizing (TODAY)

#### 1. Settings Tab
- [ ] Account size input (default $10,000)
- [ ] Risk % slider (2-5%, default 2%)
- [ ] Persist settings to localStorage
- [ ] Display current configuration

#### 2. Position Sizing Calculator
- [ ] Input: Entry price, Stop price, Ticker
- [ ] Calculate: Position size, $ Risk, # Shares
- [ ] Formula: `Shares = (Account × Risk%) / (Entry - Stop)`
- [ ] Show actual $ amount at risk
- [ ] Visual display of position parameters

### Phase 2: Future Features (Deferred)

#### Trade Journal with R-Multiple Tracking
- Log trades with Entry, Stop, Target
- Track outcome in R-multiples
- Calculate running expectancy
- SQN (System Quality Number) calculation

#### Keep Existing System
- Move 75-point analysis to separate "Research" tab
- Use for long-term positional trading research
- May prove useful for different timeframes

---

## USER PARAMETERS

| Parameter | Value | Notes |
|-----------|-------|-------|
| Account Size | $10,000 | Configurable |
| Risk per Trade | 2% | Range: 2-5%, configurable |
| Max Risk Amount | $200 | At 2% risk |
| Monitoring Frequency | 3-4 days/week | Swing trading compatible |

---

## ARCHITECTURE CHANGE

### Before (Day 1-27): Signal-Focused
```
Input: Ticker
↓
Technical Analysis → Score (75 pts)
↓
Output: BUY/HOLD/AVOID
```

### After (Day 28+): Risk-Focused
```
Input: Ticker + Entry + Stop
↓
Position Sizing → How many shares at X% risk?
↓
Output: Position Size, $ Risk, R:R ratio
↓
Journal → Track results in R-multiples
```

---

## KEY FILES

### New/Modified Day 27
| File | Purpose |
|------|---------|
| `frontend/src/utils/simplifiedScoring.js` | 4 binary criteria system |
| `backend/backtest/backtest_technical.py` | 75-point backtest |
| `backend/backtest/backtest_simplified.py` | Simplified system backtest |
| `frontend/src/App.jsx` | Added simplified view toggle |

### To Create Day 28
| File | Purpose |
|------|---------|
| `frontend/src/components/Settings.jsx` | Account/risk configuration |
| `frontend/src/components/PositionCalculator.jsx` | Position sizing calculator |
| `frontend/src/utils/positionSizing.js` | Position sizing formulas |

---

## VAN THARP PRINCIPLES (Reference)

1. **R-Multiple:** (Exit - Entry) / (Entry - Stop)
2. **Expectancy:** (Win% × AvgWin) + (Loss% × AvgLoss) in R
3. **Position Size:** Account × Risk% / Risk per Share
4. **SQN:** (Mean R / StdDev R) × sqrt(N)
5. **Holy Grail:** Not finding perfect entry, but managing risk

---

## QUICK START

```bash
# Backend
cd /Users/balajik/projects/swing-trade-analyzer/backend
source venv/bin/activate
python backend.py

# Frontend
cd /Users/balajik/projects/swing-trade-analyzer/frontend
npm start
```

---

*Previous: Day 27 - System Validation (REJECTED 55% hypothesis)*
*Next: Day 29 - Trade Journal & R-Multiple Tracking*
