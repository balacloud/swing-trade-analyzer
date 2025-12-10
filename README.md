# 🎯 Swing Trade Analyzer

An institutional-grade swing trade recommendation engine that analyzes stocks and provides data-driven verdicts based on proven methodologies from **Mark Minervini (SEPA)** and **William O'Neil (CAN SLIM)**.

![Version](https://img.shields.io/badge/version-1.0-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Validation](https://img.shields.io/badge/validation-80%25%20pass-blue)

---

## 📊 What It Does

1. **Enter a stock ticker** (e.g., AAPL, NVDA, AVGO)
2. **System fetches real market data** from yfinance + Defeat Beta
3. **Calculates 75-point score** across 4 categories
4. **Generates verdict:** BUY / HOLD / AVOID
5. **Quality gates** flag critical issues (downtrend, low liquidity, etc.)

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    SWING TRADE ANALYZER                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  TECHNICAL DATA (yfinance - 15-30 min delay)                │
│  ├── Price, 50 SMA, 200 SMA, 8 EMA, 21 EMA                  │
│  ├── Volume                                                 │
│  └── RS Calculation (stock return vs SPY return)            │
│                                                              │
│  FUNDAMENTAL DATA (Defeat Beta - Weekly update)             │
│  ├── EPS Growth, Revenue Growth                             │
│  ├── ROE, Debt/Equity                                       │
│  └── Forward P/E                                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📈 Scoring Methodology (75 Points)

| Category | Points | Components |
|----------|--------|------------|
| **Technical** | 40 | Trend Structure (15), Short-term Trend (10), RS (10), Volume (5) |
| **Fundamental** | 20 | EPS Growth (6), Revenue Growth (5), ROE (4), D/E (3), P/E (2) |
| **Sentiment** | 10 | News sentiment (placeholder for v2.0) |
| **Risk/Macro** | 5 | VIX (2), S&P Regime (2), Breadth (1) |

### Verdict Logic
- **BUY:** Score ≥60 + No critical fails + RS ≥1.0
- **HOLD:** Score 40-59 OR 1 critical fail
- **AVOID:** Score <40 OR 2+ critical fails OR RS <0.8

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- Git

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python backend.py
```
Backend runs on `http://localhost:5001`

### Frontend Setup
```bash
cd frontend
npm install
npm start
```
Frontend runs on `http://localhost:3000`

---

## 📁 Project Structure

```
swing-trade-analyzer/
├── backend/
│   ├── backend.py              # Flask API server
│   ├── requirements.txt        # Python dependencies
│   └── venv/                   # Virtual environment
│
└── frontend/
    ├── src/
    │   ├── App.jsx             # Main React component
    │   ├── services/
    │   │   └── api.js          # API calls to backend
    │   └── utils/
    │       ├── rsCalculator.js     # Relative Strength calculation
    │       ├── scoringEngine.js    # 75-point scoring logic
    │       └── technicalIndicators.js
    ├── package.json
    └── public/
```

---

## 🔌 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/health` | Backend health check |
| `GET /api/stock/<ticker>` | Stock data + prices |
| `GET /api/fundamentals/<ticker>` | Rich fundamentals |
| `GET /api/market/spy` | SPY data for RS calculation |
| `GET /api/market/vix` | VIX for risk assessment |

---

## ✅ Validation Status

Validated against external sources (CNBC, StockAnalysis, GuruFocus):

| Metric | Pass Rate |
|--------|-----------|
| Price Data | 100% |
| Revenue Growth | 100% |
| RS Calculation | 100% |
| ROE | 75% (weekly lag by design) |
| Debt/Equity | 75% |
| **Overall** | **80%** |

---

## 🗺️ Roadmap

| Version | Status | Features |
|---------|--------|----------|
| **v1.0** | ✅ Complete | Single stock analysis, 75-point scoring |
| **v1.1** | 🔄 In Progress | TradingView batch scanning |
| **v1.2** | 📅 Planned | Support & Resistance Engine (Entry/Stop/Target) |
| **v2.0** | 🔮 Future | Pattern detection, Backtesting |

---

## 📚 Methodology

This system is based on proven swing trading methodologies:

- **Mark Minervini's SEPA** - Stage analysis, trend templates, VCP patterns
- **William O'Neil's CAN SLIM** - Growth + momentum + institutional sponsorship

### Target Performance
- **Hold Period:** 1-2 months
- **Target Returns:** 10-20% per trade
- **Win Rate Goal:** 60-70% (aspirational, needs backtesting)

---

## 🛠️ Tech Stack

- **Frontend:** React + Tailwind CSS
- **Backend:** Python Flask
- **Data Sources:** 
  - yfinance (real-time prices)
  - Defeat Beta (fundamentals)
- **Version Control:** Git/GitHub

---

## 📄 License

This project is for educational and personal use.

---

## 🤝 Contributing

This is a personal project, but suggestions are welcome! Open an issue to discuss.

---

## 📞 Contact

- **GitHub:** [balacloud](https://github.com/balacloud)
- **Repository:** [swing-trade-analyzer](https://github.com/balacloud/swing-trade-analyzer)

---

*Built with ❤️ for swing traders who want data-driven decisions*
