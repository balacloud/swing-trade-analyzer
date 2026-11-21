"""Tests for the Tradier fallback rule (Day 129, docs/claude/design/TRADIER_FALLBACK_RULE_PLAN_DAY129.md).
Fake providers, isolated cache DB: nothing here touches the live cache, the network or the real circuit breakers."""
import io, json, os, sys, tempfile, threading
from contextlib import redirect_stdout
from datetime import datetime, timedelta
from pathlib import Path
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backtest'))
import cache_manager as cm
import data_quality as dq
from providers import orchestrator as orch
from providers.exceptions import ProviderError
from providers.fallback_policy import NO_TRADIER, tradier_blocked

passed = failed = 0
def ok(cond, msg):
    global passed, failed
    if cond: passed += 1
    else:
        failed += 1; print(f'FAIL {msg}')

def quiet(fn, *a, **k):
    buf = io.StringIO()
    with redirect_stdout(buf): out = fn(*a, **k)
    return out, buf.getvalue()

def frame(n=504, last='2026-11-19', seed=3):
    r = np.random.default_rng(seed); idx = pd.bdate_range(end=last, periods=n); c = 100 + np.cumsum(r.normal(0, 1, n))
    return pd.DataFrame({'open': c, 'high': c + 1, 'low': c - 1, 'close': c, 'volume': np.full(n, 1e6)}, index=idx)

tmp = tempfile.mkdtemp(); cm.DB_PATH = Path(tmp) / 'cache.db'
for _n in ('init_database', 'init_db', 'initialize_database', 'init_cache'):
    if hasattr(cm, _n): getattr(cm, _n)(); break

class Res:
    def __init__(self, df, src): self.df, self.source, self.rows = df, src, len(df)
class Fake:
    def __init__(self, name, fail=True): self.name, self.fail, self.calls = name, fail, 0
    def get_ohlcv(self, t, period):
        self.calls += 1
        if self.fail: raise ProviderError(self.name, 'down', t)
        return Res(frame(), self.name)

def make(td_fail=True, yf_fail=True, tr_fail=False):
    dp = orch.DataProvider.__new__(orch.DataProvider)
    dp._ohlcv_locks = {}; dp._ohlcv_locks_guard = threading.Lock(); dp._last_source = {}
    dp.td, dp.yf, dp.tr = Fake('twelvedata', td_fail), Fake('yfinance', yf_fail), Fake('tradier', tr_fail)
    dp._ohlcv_chain = [dp.td, dp.yf, dp.tr]; dp._deliver = lambda t, df: df
    return dp

# ---- the list
ok(tradier_blocked('nvdl') and tradier_blocked('QPUX') and tradier_blocked('GDXU.TO') and tradier_blocked('SOXL.NE'), 'listed funds are blocked (case-insensitive)')
ok(not tradier_blocked('JNJ') and not tradier_blocked('AAPL') and not tradier_blocked('') and not tradier_blocked(None), 'plain stocks, empty and None are not blocked')

# ---- blocked ticker: Tradier is never asked
orch._chain_failures.clear()
dp = make()
try: quiet(dp.get_ohlcv, 'NVDL', '2y'); got = 'served'
except ProviderError as e: got = 'error'
ok(got == 'error', 'blocked ticker, Twelve Data and Yahoo down, no saved copy: a clear error')
ok(dp.tr.calls == 0, 'Tradier received ZERO calls for a blocked ticker')
ok(dp.td.calls == 1 and dp.yf.calls == 1, 'Twelve Data and Yahoo were each tried once')
# memo: the repeat within 60 s makes no provider call
try: quiet(dp.get_ohlcv, 'NVDL', '2y')
except ProviderError as e: msg = str(e)
ok(dp.td.calls == 1 and dp.yf.calls == 1, 'repeat within 60 s makes no provider calls (failure memo)')
ok('not retried' in msg, 'the repeat error says it was not retried')
orch._chain_failures['NVDL'] = (orch.time.monotonic() - 61, 'old')
try: quiet(dp.get_ohlcv, 'NVDL', '2y')
except ProviderError: pass
ok(dp.td.calls == 2 and dp.yf.calls == 2, 'after 60 s the chain is tried again')
# a recovered source works at once (no stale memo blocking a good fetch)
dp.td.fail = False; orch._chain_failures['NVDL'] = (orch.time.monotonic() - 61, 'old')
out, _ = quiet(dp.get_ohlcv, 'NVDL', '2y')
ok(len(out) == 504 and dp._last_source['NVDL_ohlcv'] == 'twelvedata', 'a recovered Twelve Data serves the blocked ticker')

# ---- plain ticker: Tradier still last resort
orch._chain_failures.clear(); dp = make()
out, _ = quiet(dp.get_ohlcv, 'JNJ', '2y')
ok(dp.tr.calls == 1 and dp._last_source['JNJ_ohlcv'] == 'tradier' and len(out) == 504, 'plain ticker: Tradier is still the last resort and serves')
orch._chain_failures.clear(); dp = make(); dp.tr.fail = True
try: quiet(dp.get_ohlcv, 'XYZ', '2y')
except ProviderError: pass
try: quiet(dp.get_ohlcv, 'XYZ', '2y')
except ProviderError: pass
ok(dp.td.calls == 2, 'plain ticker: no failure memo (only blocked tickers get one)')

# ---- stale copies
orch._chain_failures.clear()
quiet(cm.set_cached_ohlcv, 'URAA', frame(), '2y', 'tradier')
conn = cm.get_db_connection(); conn.execute("UPDATE ohlcv_cache SET expires_at=? WHERE ticker='URAA'", ((datetime.now(cm.ET) - timedelta(hours=3)).isoformat(),)); conn.commit(); conn.close()
dp = make()
try: quiet(dp.get_ohlcv, 'URAA', '2y'); got = 'served'
except ProviderError: got = 'error'
ok(got == 'error' and dp.tr.calls == 0, 'a stale TRADIER copy of a blocked ticker is refused')
quiet(cm.set_cached_ohlcv, 'SOXL', frame(), '2y', 'yfinance')
conn = cm.get_db_connection(); conn.execute("UPDATE ohlcv_cache SET expires_at=? WHERE ticker='SOXL'", ((datetime.now(cm.ET) - timedelta(days=40)).isoformat(),)); conn.commit(); conn.close()
dp = make()
out, log = quiet(dp.get_ohlcv, 'SOXL', '2y')
ok(len(out) == 504 and dp._last_source['SOXL_ohlcv'] == 'stale_cache' and dp.tr.calls == 0, 'a stale Yahoo copy of a blocked ticker (any age) is still served')
quiet(cm.set_cached_ohlcv, 'KO', frame(), '2y', 'tradier')
conn = cm.get_db_connection(); conn.execute("UPDATE ohlcv_cache SET expires_at=? WHERE ticker='KO'", ((datetime.now(cm.ET) - timedelta(hours=3)).isoformat(),)); conn.commit(); conn.close()
dp = make(); dp.tr.fail = True
out, _ = quiet(dp.get_ohlcv, 'KO', '2y')
ok(len(out) == 504 and dp._last_source['KO_ohlcv'] == 'stale_cache', 'a stale Tradier copy of a PLAIN ticker is still served')

# ---- tab check
base = frame(260, last='2026-11-19')
facts = dq.check_history(base, now=datetime(2026, 11, 20, 12, 0, tzinfo=dq.MARKET_TZ) if hasattr(dq, 'MARKET_TZ') else None, ticker='T')
q = dq.quality_level(facts)
ok('source' not in q['checks'], 'no source argument: no new check (old callers unchanged)')
for src in ('twelvedata', 'yfinance', 'cache', None):
    ok('source' not in dq.quality_level(facts, source=src)['checks'], f'source {src}: no extra row')
qt = dq.quality_level(facts, source='tradier')
ok(qt['checks']['source']['level'] == 'WARN' and 'backup' in qt['checks']['source']['note'], 'Tradier-served plain ticker: WARN that names the backup source')
ok('dividend' in qt['checks']['source']['note'], 'the WARN says prices are not dividend-adjusted')
qb = dq.quality_level(facts, source='tradier', blocked=True)
ok(qb['checks']['source']['level'] == 'FAIL' and qb['level'] == 'FAIL', 'Tradier-served blocked ticker: FAIL, overall FAIL')
ok(dq.quality_level({'state': 'error', 'reason': 'x'}, source='tradier')['level'] == 'FAIL', 'a failed history still FAILs with a source given')

# ---- drift: every leveraged fund the audit knows is on the list
import audit_data_sources as ads
lev = [s for (cls, s, why) in ads.UNIVERSE if 'leverag' in cls.lower()]
ok(len(lev) >= 5, f'the hand-labelled audit universe has its leveraged funds ({len(lev)})')
_rows = Path(os.path.dirname(os.path.abspath(__file__))) / 'validation_results' / 'data_audit_20261119_pm.json'
if _rows.exists():      # the 117-ticker run (untracked data): its class column is the wider list
    lev = sorted(set(lev) | {r['symbol'] for r in json.load(open(_rows))['rows'] if 'leverag' in r['class'].lower()})
    ok(len(lev) >= 19, f'the 117-ticker audit has at least 19 leveraged funds ({len(lev)})')
ok(all(s in NO_TRADIER for s in lev), f'every audit-universe leveraged fund is in NO_TRADIER (missing: {[s for s in lev if s not in NO_TRADIER]})')
cache_file = Path(os.path.dirname(os.path.abspath(__file__))) / 'validation_results' / 'instrument_class_cache.json'
if cache_file.exists():
    c = json.load(open(cache_file))
    names = [s for s, v in c.items() if dq.classify_instrument(v.get('quote_type'), v.get('name'))['class'] == 'Leveraged ETF']
    ok(all(s in NO_TRADIER for s in names), f'every name-classified leveraged ETF is in NO_TRADIER (missing: {[s for s in names if s not in NO_TRADIER]})')


# ---- audit C8 reads what the tab shows
def _f(n=300, bad=0, last='2026-11-19'):
    d = frame(n, last=last)
    for i in range(bad):
        d.iloc[10 + i, d.columns.get_loc('low')] = d['close'].iloc[10 + i] + 5      # low above close = malformed bar
    return d
ads.TODAY = datetime(2026, 11, 20, 12, 0, tzinfo=ads.MARKET_TZ)
good, badf = _f(), _f(bad=5)
fr = {'twelvedata': good, 'yfinance': good, 'tradier': badf}
tab = {'source': 'tradier', 'rows': 300, 'status': 'just_fetched'}
r, _ = quiet(ads.grade, 'NEE', fr, {**tab, 'quality_checks': ['integrity', 'source']})
ok(r['C8'][0] == 'WARN' and 'already lists' in r['C8'][1], 'C8: bad data but the tab lists integrity: WARN "already lists", not "no warning"')
r, _ = quiet(ads.grade, 'NEE', fr, {**tab, 'quality_checks': ['source']})
ok(r['C8'][0] == 'FAIL' and 'does not list' in r['C8'][1], 'C8: bad data and the tab lists only the source: FAIL "does not list"')
r, _ = quiet(ads.grade, 'NEE', fr, {**tab, 'quality_checks': ['integrity']})
ok(r['C8'][0] == 'FAIL' and 'backup source' in r['C8'][1], 'C8: Tradier served but the tab has no source row: FAIL')
r, _ = quiet(ads.grade, 'NEE', fr, tab)
ok(r['C8'][0] == 'FAIL' and 'shows no warning' in r['C8'][1], 'C8: an old saved claim without quality_checks keeps the old wording')
fr2 = {'twelvedata': good, 'yfinance': good, 'tradier': good}
r, _ = quiet(ads.grade, 'JNJ', fr2, {**tab, 'quality_checks': ['source']})
ok(r['C8'][0] in ('PASS', 'WARN') and 'backup' not in r['C8'][1], 'C8: clean Tradier data with the source row shown is not a FAIL')

print(f'{passed} passed, {failed} failed')
sys.exit(0 if failed == 0 else 1)
