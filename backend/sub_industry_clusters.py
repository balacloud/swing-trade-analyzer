"""
Sub-industry theme cluster -> proxy ETF mapping, for the Sectors tab's
"Sub-Industry Watch" section (Day 100+). Transcribed from the Trading
Intelligence Hub's `research/sector_advisory/ticker_themes.py` (not imported
cross-repo — this is a separate git project; keeping STA self-contained), a
hand-curated, live-Tradier-verified proxy-ETF-per-theme mapping the Hub built
for its own advisory panel.

This is the level nothing else in STA computes: STA's own /api/sectors/rotation
stops at the 11 broad GICS sectors, which is too coarse to show a genuinely
sector-specific move (e.g. a semis-only selloff shows up there only as a soft
"XLK: Weakening"). These 21 clusters (all with a real, tradeable proxy ETF)
fill that gap using STA's own existing RS-ratio/quadrant formula
(compute_rs_ratio_and_quadrant() in backend.py) — not a second, differently
-normalized implementation.

Each cluster's `tickers` list is informational context only (what stock names
this theme represents) — not currently used to drive any calculation; only
`proxy` is fetched. Imperfect-fit proxies (e.g. WGMI for the whole Crypto
basket, XLK doing double duty for Optical/Connectivity and Enterprise Tech)
are inherited as-is from the Hub's own disclosed judgment calls.
"""
from __future__ import annotations

SUB_INDUSTRY_CLUSTERS = {
    "Semis": {
        "proxy": "SMH",
        "tickers": ["NVDA", "AMD", "MU", "MRVL", "AVGO", "SMCI", "ARM", "ON",
                    "QCOM", "TSM", "AMAT", "LRCX", "KLAC", "ASML", "LSCC", "ALAB"],
    },
    "Memory/Storage": {
        "proxy": "DRAM",
        "tickers": ["WDC"],
    },
    "AI Infra/Power": {
        "proxy": "GRID",
        "tickers": ["CEG", "ETN", "ANET", "ABB", "GEV", "VRT", "PWR", "MOD"],
    },
    "Nuclear/Uranium": {
        "proxy": "URA",
        "tickers": ["CCJ", "OKLO", "BWXT"],
    },
    "Critical Materials": {
        "proxy": "COPX",
        "tickers": ["ALB", "FCX", "MP", "TECK"],
    },
    "Gold Miners": {
        "proxy": "GDX",
        "tickers": [],  # GDX itself IS the theme
    },
    "Biotech": {
        "proxy": "XBI",
        "tickers": [],  # XBI itself IS the theme
    },
    "Financials/Fintech": {
        "proxy": "XLF",
        "tickers": ["GS", "PYPL", "HOOD", "SOFI", "AFRM", "UPST"],
    },
    "Crypto": {
        "proxy": "WGMI",  # precise for HIVE/MARA/RIOT, looser for COIN/MSTR — disclosed imperfection
        "tickers": ["HIVE", "MARA", "RIOT", "COIN", "MSTR"],
    },
    "Software/SaaS": {
        "proxy": "IGV",
        "tickers": ["PLTR", "CRWD", "SNOW", "NET", "SHOP", "DDOG", "PATH", "GIB"],
    },
    "China Internet ADR": {
        "proxy": "KWEB",
        "tickers": ["BABA", "PDD", "JD"],
    },
    "EV/Autonomous": {
        "proxy": "DRIV",
        "tickers": ["NIO", "LI", "XPEV", "RIVN"],
    },
    "Space/Emerging": {
        "proxy": "UFO",
        "tickers": ["LUNR", "RKLB", "ASTS"],
    },
    "Optical/Connectivity": {
        "proxy": "XLK",  # no optical-specific liquid ETF exists; broad-tech fallback, disclosed
        "tickers": ["GLW", "APH", "FN"],
    },
    "Enterprise Tech": {
        "proxy": "XLK",
        "tickers": ["DELL", "HPE", "HPQ", "KEYS"],
    },
    "Communication Services": {
        "proxy": "XLC",
        "tickers": ["TMUS", "NFLX"],
    },
    "Defense": {
        "proxy": "ITA",
        "tickers": ["NOC"],
    },
    "Physical AI/Robotics": {
        "proxy": "BOTZ",
        "tickers": ["CGNX", "ISRG"],
    },
    "Industrials/Water": {
        "proxy": "PHO",
        "tickers": ["XYL"],
    },
    "Energy": {
        "proxy": "XLE",
        "tickers": ["OXY", "TRP"],
    },
    "High-beta mega": {
        "proxy": "XLY",  # TSLA's actual GICS sector (Consumer Discretionary)
        "tickers": ["TSLA"],
    },
}

# No thematic ETF fits cleanly — reported informationally, never given a guessed proxy.
NO_PROXY_CLUSTERS = {
    "Past survivors": {
        "tickers": ["POET"],
    },
}
