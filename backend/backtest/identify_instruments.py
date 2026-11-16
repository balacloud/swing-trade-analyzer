"""
Step 0 of the data-source testing plan (docs/claude/design/DATA_SOURCE_TESTING_PLAN_DAY126.md):
work out WHAT each instrument on the user's IBKR watchlists is, from evidence.

The same symbol can be several instruments (US SOXL vs Canadian BetaPro SOXL, AMD vs AMD CDR).
So each row is matched by PRICE: the last price pasted from IBKR vs the last close of every
candidate Yahoo listing (US, Toronto .TO, Cboe Canada .NE, TSX Venture .V). The listing whose
price agrees (within TOLERANCE) is the instrument. Exchange, currency and quote type come from
Yahoo for that listing. Class (stock / ETF / leveraged / CDR) comes from Yahoo's quote type plus
the IBKR description and the user's own list names. Nothing is assumed from the symbol alone.

Prices below were pasted by the user on 2026-11-13/14 (IBKR watchlist screens). They are a
snapshot and can differ from the last Yahoo close by a day's move, hence the wide tolerance.

Run: cd backend && venv/bin/python backtest/identify_instruments.py
Writes: docs/claude/design/INSTRUMENT_MASTER_DAY126.md and
        backend/validation_results/instrument_master_20261114.json
"""
import json
import os
import re
import sys
import time
from collections import defaultdict

import yfinance as yf

BACKEND = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(BACKEND)
TOLERANCE = 0.12          # a snapshot can be a day's move away (3x funds move 15%)
DELAY = 0.35              # seconds between Yahoo calls (Golden Rule 25: be gentle)

# (list, IBKR symbol, IBKR description, pasted last price or None)
ROWS = [
    # --- Quality_US_Canada (10 symbols)
    ('Quality_US_Canada', 'CAT', 'CATERPILLAR INC', 596.12),
    ('Quality_US_Canada', 'BRK B', 'BERKSHIRE HATHAWAY INC-CL B', 592.30),
    ('Quality_US_Canada', 'GOOGL', 'ALPHABET INC-CL A', 294.05),
    ('Quality_US_Canada', 'JPM', 'JPMORGAN CHASE & CO', 344.79),
    ('Quality_US_Canada', 'JNJ', 'JOHNSON & JOHNSON', 286.67),
    ('Quality_US_Canada', 'RY', 'ROYAL BANK OF CANADA', 288.37),
    ('Quality_US_Canada', 'CNR', 'CANADIAN NATL RAILWAY CO', 181.29),
    ('Quality_US_Canada', 'ATD', 'ALIMENTATION COUCHE-TARD INC', 82.85),
    ('Quality_US_Canada', 'CNQ', 'CANADIAN NATURAL RESOURCES', 70.91),
    ('Quality_US_Canada', 'CSU', 'CONSTELLATION SOFTWARE INC', 3492.29),
    # --- Long_Term_Quality_ETFs (5)
    ('Long_Term_Quality_ETFs', 'HXQ', 'GLOBAL X NASDAQ-100 INDE-CAD', 114.73),
    ('Long_Term_Quality_ETFs', 'VFV', 'VANGUARD S&P 500 INDEX ETF', 191.40),
    ('Long_Term_Quality_ETFs', 'XEQT', 'ISHARES CORE EQUITY ETF PORT', 45.52),
    ('Long_Term_Quality_ETFs', 'XCHP', 'ISHARES SEMICONDUCTOR ETF', 111.07),
    ('Long_Term_Quality_ETFs', 'FINN', 'FIDELITY GL INNOVATORS ETF', 32.71),
    # --- AI Supply Chain (26)
    ('AI Supply Chain', 'WDC', 'WESTERN DIGITAL CORP', 17.88),
    ('AI Supply Chain', 'GEV', 'GE VERNOVA INC', 790.01),
    ('AI Supply Chain', 'TSM', 'TAIWAN SEMICONDUCTOR-SP ADR', 394.50),
    ('AI Supply Chain', 'ETN', 'EATON CORP PLC', 350.00),
    ('AI Supply Chain', 'VRT', 'VERTIV HOLDINGS CO-A', 197.44),
    ('AI Supply Chain', 'CCO', 'CAMECO CORP', 100.80),
    ('AI Supply Chain', 'ASML', 'ASML HOLDING NV', 44.30),
    ('AI Supply Chain', 'ANET', 'ARISTA NETWORKS INC', 35.25),
    ('AI Supply Chain', 'CEG', 'CONSTELLATION ENERGY', 278.20),
    ('AI Supply Chain', 'ALAB', 'ASTERA LABS INC', 216.35),
    ('AI Supply Chain', 'NVDA', 'NVIDIA CORP', 161.01),
    ('AI Supply Chain', 'AVGO', 'BROADCOM INC', 340.12),
    ('AI Supply Chain', 'KEYS', 'KEYSIGHT TECHNOLOGIES IN', 291.19),
    ('AI Supply Chain', 'MU', 'MICRON TECHNOLOGY INC', 33.99),
    ('AI Supply Chain', 'GIB.A', 'CGI INC', 116.83),
    ('AI Supply Chain', 'MRVL', 'MARVELL TECHNOLOGY INC', 152.59),
    ('AI Supply Chain', 'ONTO', 'ONTO INNOVATION INC', 197.03),
    ('AI Supply Chain', 'CAMT', 'CAMTEK LIMITED', 101.50),
    ('AI Supply Chain', 'AMD', 'ADVANCED MICRO DEVICES', 521.20),
    ('AI Supply Chain', 'ORCL', 'ORACLE CORP', 123.35),
    ('AI Supply Chain', 'FCX', 'FREEPORT-MCMORAN INC', 59.27),
    ('AI Supply Chain', 'QCOM', 'QUALCOMM INC', 170.90),
    ('AI Supply Chain', 'SNDK', 'SANDISK CORP/DE', 21.41),
    ('AI Supply Chain', 'GEV', 'GE VERNOVA INC-CDR', 53.67),
    ('AI Supply Chain', 'AVGO', 'BROADCOM INC-CDR', 13.14),
    ('AI Supply Chain', 'AMD', 'ADVANCED MICRO DEVICES CDR', 13.76),
    # --- AI Supply Chain ETF (26; XCHP already above)
    ('AI Supply Chain ETF', 'HURA', 'GLOBAL X URANIUM INDEX ETF', 39.02),
    ('AI Supply Chain ETF', 'XGD', 'ISHARES S&P/TSX GLOBAL GOLD', 52.40),
    ('AI Supply Chain ETF', 'MTRX', 'GLOBAL X AI INFRAS INDX', 30.59),
    ('AI Supply Chain ETF', 'ORBX', 'GLOBAL X SPCE TECH INDEX ETF', 15.32),
    ('AI Supply Chain ETF', 'RBOT', 'GLB X ROBOTICS &AI INDEX ETF', 28.59),
    ('AI Supply Chain ETF', 'XDRV', 'ISHARES GL ELECTRIC & AU VEH', 40.87),
    ('AI Supply Chain ETF', 'CARS', 'EVOLVE AUTOMOBILE INNOVATION', 21.04),
    ('AI Supply Chain ETF', 'COPP', 'GLOBAL X COPPER PRODUCER IND', 49.57),
    ('AI Supply Chain ETF', 'UFO', 'PROCURE SPACE ETF', 40.00),
    ('AI Supply Chain ETF', 'QTUM', 'DEFIANCE QUANTUM ETF', 128.74),
    ('AI Supply Chain ETF', 'BOTZ', 'GLOBAL X ROBOTICS & ARTIFICI', 31.03),
    ('AI Supply Chain ETF', 'DRIV', 'GLOBAL X AUTONOMOUS&ELEC-ETF', 28.40),
    ('AI Supply Chain ETF', 'GDX', 'VANECK GOLD MINERS ETF', 81.52),
    ('AI Supply Chain ETF', 'DRAM', 'ROUNDHILL MEMORY ETF', 41.66),
    ('AI Supply Chain ETF', 'XETM', 'ISH ENRGY TRANSITION MAT ETF', 65.54),
    ('AI Supply Chain ETF', 'SETM', 'SPROTT CRITICAL MATERIAL ETF', 23.70),
    ('AI Supply Chain ETF', 'SMH', 'VANECK SEMICONDUCTOR ETF', 481.53),
    ('AI Supply Chain ETF', 'GRID', 'FIRST TRST NASD CL EDG SGIIF', 159.82),
    ('AI Supply Chain ETF', 'URA', 'GLOBAL X URANIUM ETF', 31.74),
    ('AI Supply Chain ETF', 'AIPO', 'DEFIANCE AI & POWER INFR ETF', 23.35),
    ('AI Supply Chain ETF', 'COPX', 'GLOBAL X COPPER MINERS ETF', 69.26),
    ('AI Supply Chain ETF', 'SOXX', 'ISHARES SEMICONDUCTOR ETF', 146.66),
    ('AI Supply Chain ETF', 'SGRD', 'FRST TRST NSD CLN EDG SG ETF', 18.47),
    ('AI Supply Chain ETF', 'SOXL', 'DIREX DAIL SEMI BU 3X ET-USD', 55.68),
    ('AI Supply Chain ETF', 'SOXL', 'BETAPRO 3X SC DAILY LEV BA', 14.72),
    # --- the 8-symbol Canadian list (user paste; list name not in the paste)
    ('Canadian list (8)', 'MDA', 'MDA SPACE LTD', 41.25),
    ('Canadian list (8)', 'NTR', 'NUTRIEN LTD', 101.62),
    ('Canadian list (8)', 'ASTL', 'ALGOMA STEEL GROUP INC', 7.79),
    ('Canadian list (8)', 'BDT', 'BIRD CONSTRUCTION INC', 76.69),
    ('Canadian list (8)', 'PNG', 'KRAKEN ROBOTICS INC', 3.40),
    ('Canadian list (8)', 'CGY', 'CALIAN GROUP LTD', 85.55),
    # --- AI_Leveraged (from the user's earlier IBKR screenshot + watchlist 122)
    ('AI_Leveraged', 'SOXL', 'BETAPRO 3X SC DAILY LEV BA', 14.22),
    ('AI_Leveraged', 'QPUX', 'DFINC 2X D LNG PURE QUNT ETF', 4.23),
    ('AI_Leveraged', 'DRAL', 'DEF DLY TGT 2X LG DRAM ETF', 4.77),
    ('AI_Leveraged', 'SPCL', 'DEFIANC DAILY 2X SPC ETF-USD', 11.93),
    ('AI_Leveraged', 'URAA', 'DIR DA URA IND BU 2X ETF-USD', 12.25),
    ('AI_Leveraged', 'UBOT', 'DD RA INT & AUTO IB 2X ETF-U', 16.60),
    ('AI_Leveraged', 'COPZ', 'DEFIANCE DAILY TARGET 2X LON', 9.77),
    ('AI_Leveraged', 'GDXU', 'BETAPRO CANADIAN GOLD MINERS', 26.36),
    ('AI_Leveraged', 'AVGC', '(no description or price in the paste)', None),
]
LEVERAGE_RE = re.compile(r'\b(2X|3X)\b|DAILY|\bDLY\b|\bLEV\b|\bD LNG\b|\bDA\b.*\b(2X|3X)\b', re.I)


def yahoo_candidates(sym):
    """Yahoo forms to try for an IBKR symbol. IBKR writes 'BRK B' / 'GIB.A'; Yahoo wants dashes."""
    base = sym.replace(' ', '-').replace('.', '-')
    if '-' in base:                       # share-class names: US form and Toronto form
        return [(base, 'US'), (base + '.TO', 'TSX'), (base + '.NE', 'Cboe Canada'), (base + '.V', 'TSX Venture')]
    return [(base, 'US'), (base + '.TO', 'TSX'), (base + '.NE', 'Cboe Canada'), (base + '.V', 'TSX Venture')]


CACHE_FILE = os.path.join(BACKEND, 'validation_results', 'instrument_probe_cache.json')
try:
    _cache = json.load(open(CACHE_FILE))
except Exception:
    _cache = {}


def probe(ysym):
    """Last close and metadata for one Yahoo symbol, or None if Yahoo has nothing."""
    if ysym in _cache:
        return _cache[ysym]
    out = None
    try:
        t = yf.Ticker(ysym)
        h = t.history(period='7d', auto_adjust=False)
        if h is not None and len(h) and not h['Close'].dropna().empty:
            fi = t.fast_info
            def g(*keys):
                for k in keys:
                    try:
                        v = fi[k]
                        if v:
                            return v
                    except Exception:
                        pass
                return None
            out = {'close': float(h['Close'].dropna().iloc[-1]), 'date': str(h.index[-1].date()),
                   'exchange': g('exchange'), 'currency': g('currency'), 'quoteType': g('quoteType', 'quote_type')}
    except Exception as e:
        print(f'   ⚠️ Yahoo error for {ysym}: {str(e)[:80]}')
    time.sleep(DELAY)
    _cache[ysym] = out
    json.dump(_cache, open(CACHE_FILE, 'w'))
    return out


CDR_RATIO = 3.0   # a CDR trades at a small fraction of its US stock (WDC 295 vs 17.9, MU 778 vs 34).
                  # A cross-listed Canadian company trades near FX parity (RY 202 USD vs 288 CAD = 0.7).


def classify(row, match, cands):
    """Leveraged first (by description or the user's AI_Leveraged list), then CDR, ETF, stock.
    CDR = the description says CDR, or a Canadian listing whose same-symbol US stock trades at more than
    CDR_RATIO times the Canadian price. That second test is an inference and is reported as such."""
    lst, sym, desc, _ = row
    listing = match['listing'] if match else None
    qt = (match or {}).get('quoteType')
    leveraged = bool(LEVERAGE_RE.search(desc)) or lst == 'AI_Leveraged'
    us = next((c for c in cands if c['listing'] == 'US'), None)
    fund_words = bool(re.search(r'\bETF\b|INDEX|\bINDE\b|ETF PORT', desc.upper()))   # a fund is never a CDR by the price test
    cdr = bool(match) and listing != 'US' and (
        'CDR' in desc.upper() or (not fund_words and us is not None and match['close'] > 0 and us['close'] / match['close'] > CDR_RATIO))
    if leveraged and 'CDR' not in desc.upper():
        kind = 'Leveraged ETF'
    elif cdr:
        kind = 'CDR (Canadian receipt of a US stock)'
    elif leveraged:
        kind = 'Leveraged ETF'
    elif qt == 'ETF' or re.search(r'\bETF\b|INDEX|ISHARES|\bIND\b|ETF PORT', desc.upper()):
        kind = 'ETF'
    elif qt == 'EQUITY':
        kind = 'Stock'
    else:
        kind = 'Unknown'
    return kind


def main():
    twins = defaultdict(int)
    for r in ROWS:
        twins[r[1]] += 1
    results = []
    seen = set()
    for row in ROWS:
        lst, sym, desc, price = row
        key = (sym, desc)
        if key in seen:
            continue
        seen.add(key)
        cands = []
        for ysym, listing in yahoo_candidates(sym):
            p = probe(ysym)
            if p:
                err = abs(p['close'] / price - 1) if price else None
                cands.append({'yahoo': ysym, 'listing': listing, **p, 'err': err})
        within = [c for c in cands if c['err'] is not None and c['err'] <= TOLERANCE]
        # The same Canadian security often trades on TSX (.TO), TSX Venture (.V) and Cboe Canada (.NE) at one price.
        # Those are venues of ONE instrument: prefer TSX, then Venture, then Cboe Canada, and list the rest.
        rank = {'TSX': 0, 'TSX Venture': 1, 'Cboe Canada': 2, 'US': 3}
        within.sort(key=lambda c: (rank[c['listing']], c['err']))
        match = within[0] if within else None
        alts = [c['yahoo'] for c in within[1:] if c['listing'] != 'US']
        markets = {('US' if c['listing'] == 'US' else 'CA') for c in within}
        status = ('AMBIGUOUS' if len(markets) > 1 else 'MATCHED' if within else
                  'NO PRICE IN PASTE' if price is None else 'UNMATCHED')
        kind = classify(row, match, cands)
        lists = sorted({r[0] for r in ROWS if (r[1], r[2]) == key})
        results.append({'ibkr_symbol': sym, 'description': desc, 'lists': lists, 'ibkr_price': price, 'status': status,
                        'sta_symbol': match['yahoo'] if match else None,
                        'listing': match['listing'] if match else None,
                        'exchange': match['exchange'] if match else None,
                        'currency': match['currency'] if match else None,
                        'yahoo_quoteType': match['quoteType'] if match else None,
                        'yahoo_close': match['close'] if match else None, 'price_diff_pct': round(match['err'] * 100, 1) if match else None,
                        'other_venues': alts, 'class': kind, 'candidates': [{k: c[k] for k in ('yahoo', 'listing', 'close', 'err')} for c in cands]})
        flag = '' if status == 'MATCHED' else f'  <-- {status}'
        print(f"{sym:6} {desc[:30]:30} paste {price}  ->  {match['yahoo'] if match else '-':9} {kind}{(' | also ' + ','.join(alts)) if alts else ''}{flag}")

    out_json = os.path.join(BACKEND, 'validation_results', 'instrument_master_20261114.json')
    with open(out_json, 'w') as f:
        json.dump({'generated': time.strftime('%Y-%m-%d %H:%M'), 'tolerance': TOLERANCE, 'rows': results}, f, indent=1)

    # ---------- Markdown
    order = ['Stock', 'ETF', 'Leveraged ETF', 'CDR (Canadian receipt of a US stock)', 'Unknown']
    def market(r):
        return 'Canada' if r['listing'] in ('TSX', 'Cboe Canada', 'TSX Venture') else ('US' if r['listing'] == 'US' else '?')
    L = ['# Instrument master: what is what (Day 126)\n',
         f"Built by `backend/backtest/identify_instruments.py` from the user's IBKR watchlist pastes (Nov 13–14) and Yahoo. "
         f"Each row is matched by **price**: the pasted IBKR last price vs the last close of every candidate Yahoo listing "
         f"(US, Toronto `.TO`, Cboe Canada `.NE`, TSX Venture `.V`), tolerance ±{int(TOLERANCE*100)}%. "
         "The listing whose price agrees is the instrument; exchange, currency and quote type are Yahoo's for that listing; "
         "class comes from Yahoo's quote type, the IBKR description and the list it sits on.\n",
         '**How to read:** `STA symbol` is what to type in STA. `Diff` is the pasted price vs Yahoo\'s last close. '
         '`AMBIGUOUS` / `UNMATCHED` rows need a human look.\n']
    counts = defaultdict(int)
    for r in results:
        counts[(market(r), r['class'])] += 1
    L.append('## Counts\n\n| Market | Stock | ETF | Leveraged ETF | CDR |\n|---|---|---|---|---|')
    for m in ('US', 'Canada', '?'):
        L.append(f"| {m} | {counts[(m,'Stock')]} | {counts[(m,'ETF')]} | {counts[(m,'Leveraged ETF')]} | {counts[(m,'CDR (Canadian receipt of a US stock)')]} |")
    flagged = [r for r in results if r['status'] != 'MATCHED']
    L.append(f"\n**{len(results)} distinct instruments, {len(results)-len(flagged)} matched cleanly, {len(flagged)} need a look.**\n")
    for kind in order:
        rows = [r for r in results if r['class'] == kind]
        if not rows:
            continue
        L.append(f'\n## {kind} ({len(rows)})\n')
        L.append('| IBKR | Description | List(s) | Paste | STA symbol | Also trades as | Market · exchange | Cur | Yahoo close | Diff | Status |')
        L.append('|---|---|---|---|---|---|---|---|---|---|---|')
        for r in sorted(rows, key=lambda x: (market(x), x['ibkr_symbol'])):
            L.append(f"| {r['ibkr_symbol']} | {r['description']} | {', '.join(r['lists'])} | {r['ibkr_price'] if r['ibkr_price'] is not None else '—'} | "
                     f"{('`'+r['sta_symbol']+'`') if r['sta_symbol'] else '—'} | {(', '.join('`'+a+'`' for a in r['other_venues'])) or '—'} | {market(r)} · {r['exchange'] or '—'} | {r['currency'] or '—'} | "
                     f"{round(r['yahoo_close'],2) if r['yahoo_close'] else '—'} | {('%+.1f%%' % ((r['yahoo_close']/r['ibkr_price']-1)*100)) if (r['yahoo_close'] and r['ibkr_price']) else '—'} | {r['status']} |")
    if flagged:
        L.append('\n## Needs a human look\n')
        for r in flagged:
            c = ', '.join(f"{x['yahoo']}={round(x['close'],2)}" for x in r['candidates']) or 'no Yahoo listing found'
            L.append(f"- **{r['ibkr_symbol']}** ({r['description']}), paste {r['ibkr_price']}: {r['status']}. Yahoo candidates: {c}")
    with open(os.path.join(REPO, 'docs', 'claude', 'design', 'INSTRUMENT_MASTER_DAY126.md'), 'w') as f:
        f.write('\n'.join(L) + '\n')
    print(f'\n{len(results)} instruments, {len(flagged)} flagged. Wrote INSTRUMENT_MASTER_DAY126.md and {out_json}')


if __name__ == '__main__':
    main()
