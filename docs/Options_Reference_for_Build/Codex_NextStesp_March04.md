<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# can you summarize this in one single markdown so that i can feed it in to codex

```markdown
# OptionsIQ v2.1 — Complete Codex Build Prompt
> Standalone Options Analysis Module | Python/Flask + React | IBKR via ib_insync
> Backend: localhost:5051 | Frontend: localhost:3050

---

## 0. Mandate

Build a fully independent options analysis module called **OptionsIQ**.
- Personal use only. No auth. No scale requirements.
- Data: Interactive Brokers API (ib_insync) → yfinance fallback → mock fallback
- IBKR IB Gateway runs locally on port 7496 (live) or 7497 (paper)
- Market data subscriptions active: US Securities Snapshot + US Equity & Options Add-On
- Later connects to a swing analyzer at localhost:5001 via clean REST seam
- **Build in Phase order. After every step: `curl localhost:5051/api/health` must return 200.**

---

## 1. Project Structure

```

optionsiq/
├── backend/
│   ├── app.py
│   ├── exceptions.py
│   ├── cache_manager.py
│   ├── circuit_breaker.py
│   ├── data_service.py
│   ├── ibkr_provider.py
│   ├── yfinance_provider.py
│   ├── mock_provider.py
│   ├── gate_engine.py
│   ├── strategy_ranker.py
│   ├── pnl_calculator.py
│   ├── bs_calculator.py
│   ├── iv_store.py
│   ├── logger_config.py
│   ├── data/
│   │   └── cache.db          \# auto-created SQLite
│   ├── logs/
│   │   ├── app.log
│   │   ├── ibkr.log
│   │   ├── cache.log
│   │   └── gates.log
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   ├── Header.jsx
│   │   │   ├── SwingImportStrip.jsx
│   │   │   ├── DirectionSelector.jsx
│   │   │   ├── MasterVerdict.jsx
│   │   │   ├── GatesGrid.jsx
│   │   │   ├── BehavioralChecks.jsx
│   │   │   ├── TopThreeCards.jsx
│   │   │   ├── PnLTable.jsx
│   │   │   └── PaperTradeBanner.jsx
│   │   ├── hooks/
│   │   │   └── useOptionsData.js
│   │   └── index.css
│   └── package.json
├── start.sh
└── stop.sh

```

---

## 2. Environment & Config

### `.env`
```

IBKR_HOST=127.0.0.1
IBKR_PORT=7496
IBKR_CLIENT_ID=10
ACCOUNT_SIZE=24813
ACCOUNT_CURRENCY=CAD
CAD_USD_RATE=0.73
RISK_PCT=0.01
PLANNED_HOLD_DAYS=7
SWING_ANALYZER_URL=http://localhost:5001
FLASK_PORT=5051
IBKR_MARKET_DATA_TYPE=1

```

### `requirements.txt`
```

flask>=3.0
flask-cors>=4.0
ib_insync>=0.9.86
yfinance>=0.2.40
numpy>=1.26
scipy>=1.12
python-dotenv>=1.0

```

---

## 3. `exceptions.py` — Typed Exception Hierarchy

```python
"""
Rule: NEVER raise bare Exception(). Always raise a typed subclass.
Rule: Every exception is recoverable OR has a defined fallback.
Rule: HTTP layer catches OptionsIQError and maps to status codes.
"""

class OptionsIQError(Exception):
    def __init__(self, message: str, context: dict = None, recoverable: bool = True):
        self.message = message
        self.context = context or {}
        self.recoverable = recoverable
        super().__init__(message)

# ── Data Source ──────────────────────────────────────────────────────────────
class IBKRError(OptionsIQError): pass

class IBKRNotConnectedError(IBKRError):
    """IB Gateway not running. recoverable=True → fallback to yfinance."""
    pass

class IBKREntitlementError(IBKRError):
    """Error 10089/10091 — subscription missing."""
    def __init__(self, data_type: str, error_code: int):
        super().__init__(
            f"IBKR entitlement missing for {data_type} (code {error_code})",
            context={"data_type": data_type, "ibkr_error": error_code},
            recoverable=True
        )

class IBKRTimeoutError(IBKRError):
    """Request exceeded timeout. recoverable=True → serve cache."""
    def __init__(self, ticker: str, timeout_s: float):
        super().__init__(
            f"IBKR timeout for {ticker} after {timeout_s}s",
            context={"ticker": ticker, "timeout": timeout_s},
            recoverable=True
        )

class IBKRRateLimitError(IBKRError):
    """Pacing violation. recoverable=True → backoff retry."""
    pass

class DataProviderError(OptionsIQError):
    """Secondary provider (yfinance etc.) failed."""
    def __init__(self, provider: str, ticker: str, reason: str):
        super().__init__(
            f"{provider} failed for {ticker}: {reason}",
            context={"provider": provider, "ticker": ticker},
            recoverable=True
        )

# ── Cache ────────────────────────────────────────────────────────────────────
class CacheError(OptionsIQError): pass

class CacheMissError(CacheError):
    """Key not in cache. recoverable=True → fetch live."""
    pass

class CacheStaleError(CacheError):
    """Entry exists but TTL expired. recoverable=True → serve stale + bg refresh."""
    def __init__(self, ticker: str, age_seconds: float, ttl: float):
        super().__init__(
            f"Cache stale for {ticker}: {age_seconds:.0f}s old (TTL={ttl}s)",
            context={"ticker": ticker, "age": age_seconds, "ttl": ttl},
            recoverable=True
        )

# ── Gate Engine ──────────────────────────────────────────────────────────────
class GateEngineError(OptionsIQError):
    """Gate calculation failed. recoverable=True → gate → WARN."""
    def __init__(self, gate_id: str, reason: str):
        super().__init__(
            f"Gate {gate_id} error: {reason}",
            context={"gate_id": gate_id},
            recoverable=True
        )

class InsufficientDataError(OptionsIQError):
    """Not enough history for calculation. recoverable=True → absolute fallback."""
    def __init__(self, what: str, required: int, available: int):
        super().__init__(
            f"Insufficient data for {what}: need {required}, have {available}",
            context={"what": what, "required": required, "available": available},
            recoverable=True
        )

# ── Input ────────────────────────────────────────────────────────────────────
class ValidationError(OptionsIQError):
    """Bad request input. recoverable=False → HTTP 400."""
    def __init__(self, field: str, reason: str):
        super().__init__(
            f"Invalid '{field}': {reason}",
            context={"field": field},
            recoverable=False
        )

class InvalidTickerError(ValidationError): pass

# ── Circuit Breaker ──────────────────────────────────────────────────────────
class CircuitOpenError(OptionsIQError):
    """Circuit open — skip provider immediately."""
    def __init__(self, provider: str, cooldown_remaining: float):
        super().__init__(
            f"Circuit OPEN for {provider}, cooldown {cooldown_remaining:.0f}s",
            context={"provider": provider, "cooldown": cooldown_remaining},
            recoverable=True
        )
```


---

## 4. `logger_config.py`

```python
import logging
import logging.handlers
import os

def setup_logging():
    os.makedirs("logs", exist_ok=True)
    fmt = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(level=logging.INFO, format=fmt, datefmt=datefmt)

    for module in ["ibkr", "cache", "gates", "app"]:
        fh = logging.handlers.RotatingFileHandler(
            f"logs/{module}.log", maxBytes=10_000_000, backupCount=5
        )
        fh.setFormatter(logging.Formatter(fmt, datefmt))
        logging.getLogger(module).addHandler(fh)

    logging.getLogger("ib_insync").setLevel(logging.WARNING)
    logging.getLogger("asyncio").setLevel(logging.WARNING)
```


---

## 5. `circuit_breaker.py`

```python
import time, threading, logging
from exceptions import CircuitOpenError

logger = logging.getLogger("app")

class CircuitBreaker:
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

    def __init__(self, name: str, failure_threshold=3, cooldown=300.0, success_threshold=2):
        self.name = name
        self.failure_threshold = failure_threshold
        self.cooldown = cooldown
        self.success_threshold = success_threshold
        self._failures = 0
        self._successes = 0
        self._state = self.CLOSED
        self._opened_at: float | None = None
        self._lock = threading.Lock()

    @property
    def state(self) -> str:
        with self._lock:
            if self._state == self.OPEN:
                if time.time() - self._opened_at >= self.cooldown:
                    self._state = self.HALF_OPEN
                    self._successes = 0
                    logger.info(f"Circuit {self.name} → HALF_OPEN")
            return self._state

    def call(self, func, *args, **kwargs):
        state = self.state
        if state == self.OPEN:
            remaining = self.cooldown - (time.time() - self._opened_at)
            raise CircuitOpenError(self.name, remaining)
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure(e)
            raise

    def _on_success(self):
        with self._lock:
            if self._state == self.HALF_OPEN:
                self._successes += 1
                if self._successes >= self.success_threshold:
                    self._state = self.CLOSED
                    self._failures = 0
                    logger.info(f"Circuit {self.name} → CLOSED")
            else:
                self._failures = 0

    def _on_failure(self, error):
        with self._lock:
            self._failures += 1
            logger.warning(f"Circuit {self.name} failure {self._failures}/{self.failure_threshold}: {error}")
            if self._failures >= self.failure_threshold:
                self._state = self.OPEN
                self._opened_at = time.time()
                logger.error(f"Circuit {self.name} → OPEN ({self.cooldown}s cooldown)")

    def reset(self):
        with self._lock:
            self._state = self.CLOSED
            self._failures = 0
            self._successes = 0
            self._opened_at = None

    def status(self) -> dict:
        return {
            "name": self.name, "state": self.state,
            "failures": self._failures,
            "cooldown_remaining": max(0, self.cooldown - (time.time() - (self._opened_at or 0)))
            if self._state == self.OPEN else 0
        }

# Global singletons — one per data source
breakers = {
    "ibkr_chain":      CircuitBreaker("ibkr_chain",      failure_threshold=3, cooldown=300),
    "ibkr_historical": CircuitBreaker("ibkr_historical",  failure_threshold=3, cooldown=300),
    "yfinance":        CircuitBreaker("yfinance",         failure_threshold=5, cooldown=120),
}
```


---

## 6. `cache_manager.py` — 3-Layer Cache

```python
"""
L1: LRU in-memory dict  — <1ms — evicted on restart
L2: SQLite cache.db     — ~5ms — survives restart, market-aware TTL
L3: Stale SQLite        — ~5ms — serve immediately + background refresh

TTL Rule: During market hours (9:30–16:00 ET) use short TTLs.
          After close / weekends use long TTLs (data frozen).
"""
import sqlite3, json, time, threading
from collections import OrderedDict
from datetime import datetime
from zoneinfo import ZoneInfo
from exceptions import CacheMissError, CacheError

ET = ZoneInfo("America/New_York")
DB_PATH = "data/cache.db"

TTL_CONFIG = {
    #           l1(s)  l2_open(s)  l2_closed(s)  l3(s)
    "chain":      (60,    60,        3600,         86400),
    "underlying": (10,    300,       3600,          7200),
    "iv_history": (None,  None,   2592000,       7776000),
    "iv_snapshot":(None,  None,    604800,       2592000),
    "hv":         (60,    60,        3600,         86400),
    "spy_regime": (60,    300,       3600,          7200),
    "earnings":   (None,  None,    604800,       2592000),
}

def is_market_open() -> bool:
    now = datetime.now(ET)
    if now.weekday() >= 5:
        return False
    return now.replace(hour=9, minute=30) <= now <= now.replace(hour=16, minute=0)

def _get_ttls(data_type: str):
    cfg = TTL_CONFIG.get(data_type, (60, 60, 3600, 86400))
    l1, l2o, l2c, l3 = cfg
    l2 = l2o if is_market_open() else l2c
    return l1, l2, l3

class LRUCache:
    def __init__(self, max_size=50):
        self._store = OrderedDict()
        self._max = max_size
        self._lock = threading.Lock()

    def get(self, key: str, ttl: int):
        with self._lock:
            if key not in self._store:
                return None
            entry = self._store[key]
            if time.time() - entry["ts"] > ttl:
                del self._store[key]
                return None
            self._store.move_to_end(key)
            return entry["data"]

    def set(self, key: str, data):
        with self._lock:
            if key in self._store:
                self._store.move_to_end(key)
            self._store[key] = {"data": data, "ts": time.time()}
            if len(self._store) > self._max:
                self._store.popitem(last=False)

    def invalidate(self, key: str):
        with self._lock:
            self._store.pop(key, None)

    def stats(self):
        with self._lock:
            return {"size": len(self._store), "max": self._max}

_l1 = LRUCache(max_size=50)

def _init_db():
    import os; os.makedirs("data", exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS cache (
            key TEXT PRIMARY KEY, data_type TEXT, ticker TEXT,
            payload TEXT NOT NULL, cached_at REAL, expires_at REAL,
            source TEXT DEFAULT 'ibkr', is_stale INTEGER DEFAULT 0)""")
        conn.execute("""CREATE TABLE IF NOT EXISTS iv_history (
            ticker TEXT, date TEXT, iv REAL, source TEXT DEFAULT 'ibkr',
            PRIMARY KEY (ticker, date))""")
        conn.execute("""CREATE TABLE IF NOT EXISTS ohlcv_daily (
            ticker TEXT, date TEXT, open REAL, high REAL, low REAL,
            close REAL, volume INTEGER, PRIMARY KEY (ticker, date))""")
        conn.execute("""CREATE TABLE IF NOT EXISTS paper_trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT, direction TEXT, strategy_rank INTEGER,
            strike REAL, expiry TEXT, premium REAL, lots INTEGER,
            account_size REAL, recorded_at TEXT, status TEXT DEFAULT 'open')""")
        conn.execute("""CREATE TABLE IF NOT EXISTS cache_stats (
            data_type TEXT PRIMARY KEY,
            hits INTEGER DEFAULT 0, misses INTEGER DEFAULT 0,
            stale_serves INTEGER DEFAULT 0)""")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_cache_ticker ON cache(ticker)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_iv_ticker ON iv_history(ticker,date)")
        conn.commit()
_init_db()

class CacheManager:
    def get(self, data_type: str, ticker: str, allow_stale=True):
        """Returns (data, source_label). Raises CacheMissError if nothing found."""
        key = f"{data_type}:{ticker}"
        l1_ttl, l2_ttl, l3_ttl = _get_ttls(data_type)

        if l1_ttl:
            hit = _l1.get(key, l1_ttl)
            if hit:
                self._stat(data_type, "hits")
                return hit, "l1_fresh"

        with sqlite3.connect(DB_PATH) as conn:
            row = conn.execute(
                "SELECT payload, cached_at, expires_at FROM cache WHERE key=?", (key,)
            ).fetchone()

        if row:
            payload, cached_at, expires_at = row
            data = json.loads(payload)
            if time.time() <= expires_at:
                if l1_ttl:
                    _l1.set(key, data)
                self._stat(data_type, "hits")
                return data, "l2_fresh"
            if allow_stale and (time.time() - cached_at) < l3_ttl:
                self._stat(data_type, "stale_serves")
                return data, "l3_stale"

        self._stat(data_type, "misses")
        raise CacheMissError(f"No cache for {data_type}:{ticker}", context={"key": key})

    def set(self, data_type: str, ticker: str, data: dict, source="ibkr"):
        key = f"{data_type}:{ticker}"
        _, l2_ttl, _ = _get_ttls(data_type)
        now = time.time()
        if TTL_CONFIG.get(data_type, (60,)):
            _l1.set(key, data)
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("""INSERT OR REPLACE INTO cache
                (key, data_type, ticker, payload, cached_at, expires_at, source, is_stale)
                VALUES (?,?,?,?,?,?,?,0)""",
                (key, data_type, ticker, json.dumps(data), now, now + l2_ttl, source))
            conn.commit()

    def invalidate(self, ticker=None, data_type=None):
        if ticker:
            _l1.invalidate(f"{data_type or '*'}:{ticker}")
        with sqlite3.connect(DB_PATH) as conn:
            if ticker and data_type:
                conn.execute("DELETE FROM cache WHERE ticker=? AND data_type=?", (ticker, data_type))
            elif ticker:
                conn.execute("DELETE FROM cache WHERE ticker=?", (ticker,))
            elif data_type:
                conn.execute("DELETE FROM cache WHERE data_type=?", (data_type,))
            conn.commit()

    def stats(self) -> dict:
        with sqlite3.connect(DB_PATH) as conn:
            rows = conn.execute("SELECT data_type, hits, misses, stale_serves FROM cache_stats").fetchall()
            count = conn.execute("SELECT COUNT(*) FROM cache").fetchone()
        return {
            "l1": _l1.stats(), "l2_entries": count,
            "hit_rates": {
                r: {"hits": r, "misses": r, "stale": r,[^1][^2][^3]
                        "hit_rate_pct": round(r / (r+r+0.001)*100, 1)}[^2][^1]
                for r in rows
            }
        }

    def _stat(self, dt, col):
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(f"""INSERT INTO cache_stats (data_type, {col}) VALUES (?,1)
                ON CONFLICT(data_type) DO UPDATE SET {col}={col}+1""", (dt,))
            conn.commit()

cache = CacheManager()
```


---

## 7. `ibkr_provider.py`

```python
"""
Connects to IB Gateway via ib_insync.
ONLY raises typed IBKRError subclasses — never bare Exception.
Does NOT cache. Does NOT fallback. Data service handles that.
"""
import logging
from ib_insync import IB, Stock, Option, util
from exceptions import IBKRNotConnectedError, IBKREntitlementError, IBKRTimeoutError, IBKRRateLimitError
import os, asyncio

logger = logging.getLogger("ibkr")
util.patchAsyncio()

class IBKRProvider:
    def __init__(self):
        self.ib = IB()
        self._connect()

    def _connect(self):
        try:
            host = os.getenv("IBKR_HOST", "127.0.0.1")
            port = int(os.getenv("IBKR_PORT", 7496))
            cid  = int(os.getenv("IBKR_CLIENT_ID", 10))
            self.ib.connect(host, port, clientId=cid, readonly=True, timeout=10)
            self.ib.reqGlobalCancel()
            mdt = int(os.getenv("IBKR_MARKET_DATA_TYPE", 1))
            self.ib.reqMarketDataType(mdt)
            logger.info(f"IBKR connected: {host}:{port} clientId={cid}")
        except Exception as e:
            logger.warning(f"IBKR connect failed: {e}")

    def is_connected(self) -> bool:
        try:
            return self.ib.isConnected()
        except Exception:
            return False

    def _ensure_connected(self):
        if not self.is_connected():
            self._connect()
        if not self.is_connected():
            raise IBKRNotConnectedError("IB Gateway not reachable")

    def get_underlying_price(self, ticker: str) -> float:
        self._ensure_connected()
        contract = Stock(ticker, "SMART", "USD")
        self.ib.qualifyContracts(contract)
        [ticker_data] = self.ib.reqTickers(contract)
        price = ticker_data.midpoint() or ticker_data.last
        if not price or price <= 0:
            raise IBKRTimeoutError(ticker, 5.0)
        return float(price)

    def get_options_chain(self, ticker: str) -> dict:
        """Returns chain with bid/ask/Greeks for strikes within 10% of spot."""
        self._ensure_connected()
        from datetime import datetime, timedelta

        underlying_price = self.get_underlying_price(ticker)
        chains = self.ib.reqSecDefOptParams(ticker, "", "STK", 0)
        if not chains:
            raise IBKREntitlementError(ticker, 10089)

        chain = next((c for c in chains if c.exchange == "SMART"), chains)
        today = datetime.today()
        viable_expiries = [
            e for e in sorted(chain.expirations)
            if 14 <= (datetime.strptime(e, "%Y%m%d") - today).days <= 60
        ][:3]

        price_low  = underlying_price * 0.90
        price_high = underlying_price * 1.10
        viable_strikes = [s for s in chain.strikes if price_low <= s <= price_high]

        contracts = []
        for exp in viable_expiries:
            for strike in viable_strikes:
                for right in ["C", "P"]:
                    contracts.append(Option(ticker, exp, strike, right, "SMART"))

        self.ib.qualifyContracts(*contracts)
        tickers = self.ib.reqTickers(*contracts[:60])  # cap at 60
        self.ib.sleep(2)

        options_data = []
        for t in tickers:
            c = t.contract
            g = t.modelGreeks or t.bidGreeks or t.askGreeks
            if not g:
                continue
            options_data.append({
                "ticker": ticker, "expiry": c.lastTradeDateOrContractMonth,
                "strike": c.strike, "right": c.right,
                "bid": t.bid, "ask": t.ask, "last": t.last,
                "delta": g.delta, "gamma": g.gamma,
                "theta": g.theta, "vega": g.vega,
                "implied_vol": g.impliedVol,
                "open_interest": t.callOpenInterest or t.putOpenInterest or 0,
                "volume": t.volume or 0,
                "bid_ask_available": (t.bid is not None and t.ask is not None and t.bid > 0)
            })

        return {
            "ticker": ticker, "underlying_price": underlying_price,
            "options": options_data, "_source": "ibkr",
            "bid_ask_available": True, "greeks_source": "ibkr"
        }

    def get_historical_iv(self, ticker: str, days: int = 252) -> list:
        self._ensure_connected()
        contract = Stock(ticker, "SMART", "USD")
        self.ib.qualifyContracts(contract)
        bars = self.ib.reqHistoricalData(
            contract, endDateTime="", durationStr=f"{days} D",
            barSizeSetting="1 day",
            whatToShow="OPTION_IMPLIED_VOLATILITY",
            useRTH=True
        )
        return [{"date": str(b.date), "iv": b.close} for b in bars]
```


---

## 8. `yfinance_provider.py`

```python
import yfinance as yf
import logging
from exceptions import DataProviderError

logger = logging.getLogger("app")

class YFinanceProvider:
    def get_options_chain(self, ticker: str) -> dict:
        try:
            stock = yf.Ticker(ticker)
            info = stock.fast_info
            underlying = info.get("last_price") or info.get("regularMarketPrice")
            if not underlying:
                raise DataProviderError("yfinance", ticker, "No price data")

            options_data = []
            for expiry in stock.options[:3]:
                chain = stock.option_chain(expiry)
                for _, row in chain.calls.iterrows():
                    options_data.append({
                        "ticker": ticker, "expiry": expiry.replace("-",""),
                        "strike": row["strike"], "right": "C",
                        "bid": row.get("bid"), "ask": row.get("ask"),
                        "last": row.get("lastPrice"),
                        "implied_vol": row.get("impliedVolatility"),
                        "open_interest": row.get("openInterest", 0),
                        "volume": row.get("volume", 0),
                        "bid_ask_available": False,
                        "delta": None, "gamma": None,
                        "theta": None, "vega": None
                    })
                for _, row in chain.puts.iterrows():
                    options_data.append({
                        "ticker": ticker, "expiry": expiry.replace("-",""),
                        "strike": row["strike"], "right": "P",
                        "bid": row.get("bid"), "ask": row.get("ask"),
                        "last": row.get("lastPrice"),
                        "implied_vol": row.get("impliedVolatility"),
                        "open_interest": row.get("openInterest", 0),
                        "volume": row.get("volume", 0),
                        "bid_ask_available": False,
                        "delta": None, "gamma": None,
                        "theta": None, "vega": None
                    })
            return {
                "ticker": ticker, "underlying_price": underlying,
                "options": options_data, "_source": "yfinance",
                "bid_ask_available": False, "greeks_source": "bs_local"
            }
        except Exception as e:
            raise DataProviderError("yfinance", ticker, str(e))

    def get_underlying_price(self, ticker: str) -> float:
        try:
            info = yf.Ticker(ticker).fast_info
            return float(info.get("last_price") or info.get("regularMarketPrice"))
        except Exception as e:
            raise DataProviderError("yfinance", ticker, str(e))

    def get_historical_iv(self, ticker: str, days: int = 252) -> list:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period=f"{days}d")
            from numpy import std, log
            closes = hist["Close"].values
            returns = [log(closes[i]/closes[i-1]) for i in range(1, len(closes))]
            # Use 30-day rolling HV as IV proxy (rough fallback)
            window = 30
            result = []
            for i in range(window, len(returns)):
                hv = float(std(returns[i-window:i]) * (252**0.5) * 100)
                result.append({"date": str(hist.index[i+1].date()), "iv": hv})
            return result
        except Exception as e:
            raise DataProviderError("yfinance", ticker, str(e))

    def get_spy_regime(self) -> dict:
        try:
            spy = yf.Ticker("SPY")
            hist = spy.history(period="210d")
            closes = hist["Close"].values
            sma200 = float(sum(closes[-200:]) / 200)
            current = float(closes[-1])
            five_day_return = float((closes[-1] / closes[-6]) - 1)
            return {
                "above_200sma": current > sma200,
                "five_day_return": five_day_return,
                "spy_price": current,
                "_source": "yfinance"
            }
        except Exception as e:
            raise DataProviderError("yfinance", "SPY", str(e))
```


---

## 9. `mock_provider.py`

```python
"""Mock data for AME @ $234.35. Never raises. Used when all providers fail."""

class MockProvider:
    def get_options_chain(self, ticker: str = "AME") -> dict:
        base = 234.35
        options = [
            {"expiry":"20260417","strike":220,"right":"C","bid":14.20,"ask":14.60,"last":14.40,
             "delta":0.78,"gamma":0.015,"theta":-0.15,"vega":0.22,"implied_vol":0.172,
             "open_interest":5200,"volume":980,"bid_ask_available":True},
            {"expiry":"20260417","strike":230,"right":"C","bid":9.60,"ask":10.00,"last":9.80,
             "delta":0.68,"gamma":0.021,"theta":-0.18,"vega":0.28,"implied_vol":0.184,
             "open_interest":12400,"volume":3100,"bid_ask_available":True},
            {"expiry":"20260417","strike":235,"right":"C","bid":6.20,"ask":6.60,"last":6.40,
             "delta":0.52,"gamma":0.025,"theta":-0.22,"vega":0.34,"implied_vol":0.187,
             "open_interest":8200,"volume":2100,"bid_ask_available":True},
            {"expiry":"20260417","strike":255,"right":"C","bid":1.90,"ask":2.10,"last":2.00,
             "delta":0.24,"gamma":0.016,"theta":-0.11,"vega":0.21,"implied_vol":0.195,
             "open_interest":4100,"volume":800,"bid_ask_available":True},
            {"expiry":"20260417","strike":230,"right":"P","bid":4.80,"ask":5.20,"last":5.00,
             "delta":-0.32,"gamma":0.021,"theta":-0.14,"vega":0.28,"implied_vol":0.190,
             "open_interest":6800,"volume":1200,"bid_ask_available":True},
        ]
        for o in options:
            o["ticker"] = ticker
        return {"ticker":ticker,"underlying_price":base,"options":options,
                "_source":"mock","bid_ask_available":True,"greeks_source":"mock"}

    def get_historical_iv(self, ticker="AME", days=252) -> list:
        import random, math
        random.seed(42)
        result = []
        iv = 0.184
        for i in range(days):
            iv = max(0.12, min(0.40, iv + random.gauss(0, 0.005)))
            from datetime import date, timedelta
            d = date.today() - timedelta(days=days - i)
            result.append({"date": str(d), "iv": round(iv * 100, 2)})
        return result

    def get_underlying_price(self, ticker="AME") -> float:
        return 234.35
```


---

## 10. `bs_calculator.py`

```python
"""Black-Scholes Greeks — used when IBKR Greeks unavailable (yfinance mode)."""
from math import log, sqrt, exp
from scipy.stats import norm

RISK_FREE_RATE = 0.053  # US Fed funds approximate

def compute_greeks(S: float, K: float, T: float, sigma: float,
                   r: float = RISK_FREE_RATE, right: str = "C") -> dict:
    """
    S = underlying price, K = strike, T = years to expiry
    sigma = IV as decimal (e.g. 0.184), right = "C" or "P"
    """
    if T <= 0 or sigma <= 0 or S <= 0 or K <= 0:
        return {"delta": 0.0, "gamma": 0.0, "theta": 0.0, "vega": 0.0, "price": 0.0}
    d1 = (log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*sqrt(T))
    d2 = d1 - sigma*sqrt(T)
    if right == "C":
        delta = norm.cdf(d1)
        price = S*norm.cdf(d1) - K*exp(-r*T)*norm.cdf(d2)
        theta = (-(S*norm.pdf(d1)*sigma)/(2*sqrt(T)) - r*K*exp(-r*T)*norm.cdf(d2)) / 365
    else:
        delta = norm.cdf(d1) - 1
        price = K*exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)
        theta = (-(S*norm.pdf(d1)*sigma)/(2*sqrt(T)) + r*K*exp(-r*T)*norm.cdf(-d2)) / 365
    gamma = norm.pdf(d1) / (S * sigma * sqrt(T))
    vega  = S * norm.pdf(d1) * sqrt(T) / 100
    return {
        "delta": round(delta, 4), "gamma": round(gamma, 4),
        "theta": round(theta, 4), "vega":  round(vega, 4),
        "price": round(price, 4)
    }
```


---

## 11. `data_service.py` — Single Orchestration Layer

```python
"""
app.py ONLY calls data_service. Never calls ibkr_provider directly.
Orchestrates: Cache → CircuitBreaker → IBKR → yfinance → Mock
"""
import logging, threading
from exceptions import *
from cache_manager import cache
from circuit_breaker import breakers
from ibkr_provider import IBKRProvider
from yfinance_provider import YFinanceProvider
from mock_provider import MockProvider
from bs_calculator import compute_greeks
from datetime import datetime

logger = logging.getLogger("app")

class DataService:
    def __init__(self):
        self.ibkr = IBKRProvider()
        self.yf   = YFinanceProvider()
        self.mock = MockProvider()
        self._bg = threading.ThreadPoolExecutor(max_workers=2)

    def get_options_chain(self, ticker: str) -> dict:
        # 1. Cache
        try:
            data, src = cache.get("chain", ticker, allow_stale=False)
            return {**data, "_cache": src}
        except CacheMissError:
            pass
        except Exception:
            pass

        # 2. IBKR
        try:
            data = breakers["ibkr_chain"].call(self.ibkr.get_options_chain, ticker)
            data = self._fill_missing_greeks(data)
            cache.set("chain", ticker, data, source="ibkr")
            return {**data, "_cache": "live"}
        except CircuitOpenError as e:
            logger.warning(f"IBKR circuit open: {e}")
        except (IBKREntitlementError, IBKRTimeoutError, IBKRNotConnectedError, IBKRError) as e:
            logger.warning(f"IBKR unavailable: {e}")

        # 3. yfinance
        try:
            data = breakers["yfinance"].call(self.yf.get_options_chain, ticker)
            data = self._fill_missing_greeks(data)
            cache.set("chain", ticker, data, source="yfinance")
            return {**data, "_cache": "yfinance_live"}
        except (CircuitOpenError, DataProviderError) as e:
            logger.error(f"yfinance failed: {e}")

        # 4. Mock
        logger.warning(f"All providers failed for {ticker} — using mock")
        data = self.mock.get_options_chain(ticker)
        return {**data, "_cache": "mock"}

    def _fill_missing_greeks(self, chain: dict) -> dict:
        """Compute BS Greeks for options missing them (yfinance mode)."""
        from datetime import datetime
        S = chain["underlying_price"]
        for opt in chain.get("options", []):
            if opt.get("delta") is None and opt.get("implied_vol"):
                exp_str = str(opt["expiry"])
                try:
                    exp_date = datetime.strptime(exp_str[:8], "%Y%m%d")
                    T = max((exp_date - datetime.today()).days / 365, 0.001)
                except Exception:
                    T = 0.12
                g = compute_greeks(S, opt["strike"], T, opt["implied_vol"],
                                   right=opt.get("right", "C"))
                opt.update({"delta": g["delta"], "gamma": g["gamma"],
                            "theta": g["theta"], "vega": g["vega"]})
                if not opt.get("bid") or opt["bid"] <= 0:
                    opt["bid"] = round(g["price"] * 0.97, 2)
                    opt["ask"] = round(g["price"] * 1.03, 2)
        return chain

    def get_historical_iv(self, ticker: str, days: int = 252) -> list:
        try:
            data, _ = cache.get("iv_history", ticker)
            return data.get("history", [])
        except CacheMissError:
            pass
        try:
            hist = breakers["ibkr_historical"].call(self.ibkr.get_historical_iv, ticker, days)
            cache.set("iv_history", ticker, {"history": hist}, source="ibkr")
            return hist
        except (CircuitOpenError, IBKRError):
            pass
        try:
            hist = self.yf.get_historical_iv(ticker, days)
            cache.set("iv_history", ticker, {"history": hist}, source="yfinance")
            return hist
        except DataProviderError:
            return []

    def get_underlying_price(self, ticker: str) -> float:
        try:
            data, _ = cache.get("underlying", ticker, allow_stale=True)
            return data["price"]
        except (CacheMissError, Exception):
            pass
        try:
            price = self.ibkr.get_underlying_price(ticker)
            cache.set("underlying", ticker, {"price": price})
            return price
        except IBKRError:
            price = self.yf.get_underlying_price(ticker)
            cache.set("underlying", ticker, {"price": price}, source="yfinance")
            return price

    def get_spy_regime(self) -> dict:
        try:
            data, _ = cache.get("spy_regime", "SPY", allow_stale=True)
            return data
        except (CacheMissError, Exception):
            pass
        try:
            regime = self.yf.get_spy_regime()
            cache.set("spy_regime", "SPY", regime, source="yfinance")
            return regime
        except DataProviderError:
            return {"above_200sma": True, "five_day_return": 0.0, "_source": "default"}

    def current_mode(self) -> str:
        if self.ibkr.is_connected() and breakers["ibkr_chain"].state == "CLOSED":
            return "ibkr_live"
        if breakers["yfinance"].state != "OPEN":
            return "yfinance_delayed"
        return "mock"

    def health(self) -> dict:
        return {
            "ibkr_connected": self.ibkr.is_connected(),
            "data_mode": self.current_mode(),
            "circuit_breakers": {k: v.status() for k, v in breakers.items()},
            "cache_stats": cache.stats()
        }

    def bg_refresh(self, data_type: str, ticker: str):
        def _do():
            try:
                if data_type == "chain":
                    self.get_options_chain(ticker)
            except Exception as e:
                logger.debug(f"BG refresh failed {ticker}: {e}")
        self._bg.submit(_do)

data_service = DataService()
```


---

## 12. `gate_engine.py` — Safe Gate Wrapper + All 9 Gates (Track A)

```python
"""
Every gate is wrapped in safe_gate().
A gate calculation error → status: "warn", blocking: False.
A gate NEVER crashes the full analysis pipeline.
"""
import logging
from exceptions import InsufficientDataError, GateEngineError
from bs_calculator import compute_greeks
from cache_manager import cache

logger = logging.getLogger("gates")

GATE_RESULT = lambda id_, status, val, threshold, reason, blocking=False: {
    "id": id_, "status": status, "computed_value": val,
    "threshold": threshold, "reason": reason, "blocking": blocking
}

def safe_gate(gate_id: str, gate_func, *args, **kwargs) -> dict:
    try:
        return gate_func(*args, **kwargs)
    except InsufficientDataError as e:
        logger.warning(f"Gate {gate_id} insufficient data: {e}")
        return GATE_RESULT(gate_id, "warn", "Insufficient data", "N/A",
            f"Not enough history for {e.context.get('what')}. "
            f"Need {e.context.get('required')}, have {e.context.get('available')}.",
            blocking=False)
    except GateEngineError as e:
        logger.error(f"Gate {gate_id} error: {e}")
        return GATE_RESULT(gate_id, "warn", "Calculation error", "N/A",
            "Gate unavailable. Check logs.", blocking=False)
    except Exception as e:
        logger.exception(f"Unexpected error in gate {gate_id}")
        return GATE_RESULT(gate_id, "warn", "Error", "N/A",
            f"Unexpected: {str(e)[:80]}", blocking=False)

# ── Gate Functions ────────────────────────────────────────────────────────────

def _gate_ivr(inputs: dict, chain: dict, iv_history: list) -> dict:
    current_iv = inputs.get("current_iv") or _get_atm_iv(chain)
    if len(iv_history) >= 30:
        values = [h["iv"] for h in iv_history]
        rank = sum(1 for v in values if v <= current_iv) / len(values) * 100
        val_str = f"IVR: {rank:.0f}%"
        thresh = "< 30% to buy"
        if rank < 30:
            return GATE_RESULT("ivr","pass", val_str, thresh, "Cheap IV — ideal for buying.", blocking=False)
        elif rank < 50:
            return GATE_RESULT("ivr","warn", val_str, thresh, "Moderate IV — acceptable but elevated.", blocking=False)
        else:
            return GATE_RESULT("ivr","fail", val_str, thresh, "IV elevated — IV crush risk on entry.", blocking=True)
    else:
        # Absolute fallback
        iv_pct = current_iv * 100 if current_iv < 2 else current_iv
        if iv_pct < 20:
            return GATE_RESULT("ivr","pass",f"IV: {iv_pct:.1f}% (abs)","< 20%","Low IV — cheap to buy.",blocking=False)
        elif iv_pct < 35:
            return GATE_RESULT("ivr","warn",f"IV: {iv_pct:.1f}% (abs)","< 20%","Moderate IV.",blocking=False)
        else:
            return GATE_RESULT("ivr","fail",f"IV: {iv_pct:.1f}% (abs)","< 20%","High IV — crush risk.",blocking=True)

def _gate_hv_iv(inputs: dict, chain: dict, iv_history: list) -> dict:
    import numpy as np
    from cache_manager import DB_PATH
    import sqlite3
    ticker = inputs.get("ticker", "")
    current_iv = _get_atm_iv(chain)
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT close FROM ohlcv_daily WHERE ticker=? ORDER BY date DESC LIMIT 22",
            (ticker,)
        ).fetchall()
    if len(rows) < 21:
        raise InsufficientDataError("HV-20", 21, len(rows))
    closes = [r for r in reversed(rows)]
    log_returns = np.diff(np.log(closes))
    hv20 = float(np.std(log_returns) * np.sqrt(252) * 100)
    if hv20 < 15:
        ratio_thresh = 999  # VCP exception — skip ratio check
    else:
        ratio_thresh = 1.20
    iv_pct = current_iv * 100 if current_iv < 2 else current_iv
    ratio = iv_pct / hv20 if hv20 > 0 else 1.0
    val_str = f"IV/HV: {ratio:.2f} (IV={iv_pct:.1f}%, HV={hv20:.1f}%)"
    if ratio <= 1.20 or hv20 < 15:
        return GATE_RESULT("hv_iv","pass",val_str,"< 1.20","Options fairly priced vs realized vol.",blocking=False)
    elif ratio <= 1.30:
        return GATE_RESULT("hv_iv","warn",val_str,"< 1.20","Paying average vol risk premium.",blocking=False)
    else:
        return GATE_RESULT("hv_iv","fail",val_str,"< 1.20","IV significantly overpriced vs HV.",blocking=True)

def _gate_theta_burn(inputs: dict, best_candidate: dict) -> dict:
    premium = best_candidate.get("premium_per_lot", 0) / 100
    theta   = abs(best_candidate.get("theta_per_day", 0))
    hold    = int(inputs.get("planned_hold_days", 7))
    if premium <= 0:
        raise GateEngineError("theta_burn", "Premium is zero")
    burn_pct = (theta * hold) / premium * 100
    val_str = f"Burn: {burn_pct:.1f}% over {hold}-day hold"
    if burn_pct <= 8:
        return GATE_RESULT("theta_burn","pass",val_str,"<= 8%","Theta decay manageable.",blocking=False)
    elif burn_pct <= 12:
        return GATE_RESULT("theta_burn","warn",val_str,"<= 8%","Theta notable — need fast move.",blocking=False)
    else:
        return GATE_RESULT("theta_burn","fail",val_str,"<= 8%","Theta will erode gains — use longer DTE.",blocking=True)

def _gate_dte(inputs: dict, selected_dte: int) -> dict:
    vcp = float(inputs.get("vcp_confidence", 0))
    adx = float(inputs.get("adx", 0))
    if vcp >= 80 and adx >= 40:
        rec = 21
    elif vcp >= 60:
        rec = 45
    else:
        return GATE_RESULT("dte","fail",f"VCP confidence: {vcp:.0f}%",">= 60%",
            "VCP confidence too low. No trade recommended.",blocking=True)
    val_str = f"Selected DTE: {selected_dte}, Recommended: {rec}"
    if selected_dte >= rec - 5:
        return GATE_RESULT("dte","pass",val_str,f">= {rec} DTE","DTE adequate for setup.",blocking=False)
    elif selected_dte >= 14:
        return GATE_RESULT("dte","warn",val_str,f">= {rec} DTE","DTE below recommended — faster decay.",blocking=False)
    else:
        return GATE_RESULT("dte","fail",val_str,f">= {rec} DTE","DTE too short — high theta risk.",blocking=True)

def _gate_events(inputs: dict) -> dict:
    earnings = int(inputs.get("earnings_days_away", 999))
    dte      = int(inputs.get("selected_dte", 45))
    fomc_days = _days_to_next_fomc()
    if earnings <= dte:
        return GATE_RESULT("events","fail",f"Earnings in {earnings}d, DTE={dte}",
            "Earnings must be > DTE","Earnings within expiry window — IV crush risk.",blocking=True)
    elif fomc_days <= 5:
        return GATE_RESULT("events","warn",f"FOMC in {fomc_days}d",
            "> 5 days","FOMC approaching — volatility risk.",blocking=False)
    return GATE_RESULT("events","pass",f"Earnings {earnings}d away, FOMC {fomc_days}d",
        "Clear","No events in window.",blocking=False)

def _gate_liquidity(chain: dict, best_candidate: dict) -> dict:
    opt = best_candidate.get("_raw_option", {})
    oi     = opt.get("open_interest", 0) or 0
    vol    = opt.get("volume", 0) or 0
    prem   = best_candidate.get("premium_per_lot", 0) / 100
    bid    = opt.get("bid") or 0
    ask    = opt.get("ask") or 0
    fails  = []
    details = []
    if oi < 1000:   fails.append("OI"); details.append(f"OI={oi} < 1000")
    else:           details.append(f"OI={oi} ✓")
    vol_oi = vol / oi if oi > 0 else 0
    if vol_oi < 0.10: fails.append("Vol/OI"); details.append(f"Vol/OI={vol_oi:.2f} < 0.10")
    else:             details.append(f"Vol/OI={vol_oi:.2f} ✓")
    if prem < 2.0:    fails.append("Premium"); details.append(f"Premium=${prem:.2f} < $2")
    else:             details.append(f"Premium=${prem:.2f} ✓")
    if chain.get("bid_ask_available") and bid > 0 and ask > 0:
        spread_pct = (ask - bid) / ((bid + ask) / 2) * 100
        details.append(f"Spread={spread_pct:.1f}%")
        if spread_pct > 15: fails.append("Spread>15%")
        elif spread_pct > 10: fails.append("Spread>10%")
    else:
        details.append("Spread=N/A (awaiting entitlement)")
    val_str = " | ".join(details)
    if len(fails) == 0:
        return GATE_RESULT("liquidity","pass",val_str,"All checks","Liquid option.",blocking=False)
    elif len(fails) == 1:
        return GATE_RESULT("liquidity","warn",val_str,f"WARN: {fails}",f"Borderline: {fails}",blocking=False)
    else:
        return GATE_RESULT("liquidity","fail",val_str,f"FAIL: {fails}",f"Illiquid: {fails}",blocking=True)

def _gate_market_regime(inputs: dict) -> dict:
    above = inputs.get("spy_above_200sma", True)
    ret5  = float(inputs.get("spy_5day_return", 0.0))
    val_str = f"SPY>200SMA: {'✓' if above else '✗'} | 5d: {ret5*100:.1f}%"
    if above and ret5 > -0.02:
        return GATE_RESULT("market_regime","pass",val_str,"> -2% & above SMA","Bull regime intact.",blocking=False)
    elif above and ret5 > -0.04:
        return GATE_RESULT("market_regime","warn",val_str,"> -2% & above SMA","Weakening — reduce size.",blocking=False)
    else:
        return GATE_RESULT("market_regime","fail",val_str,"> -2% & above SMA","Bear regime — no new calls.",blocking=True)

def _gate_pivot_confirm(inputs: dict) -> dict:
    pivot = float(inputs.get("vcp_pivot", 0))
    close = float(inputs.get("last_close", 0))
    val_str = f"Last close: ${close:.2f} vs Pivot: ${pivot:.2f}"
    if close > pivot:
        return GATE_RESULT("pivot_confirm","pass",val_str,f"> ${pivot:.2f}",
            "Confirmed close above VCP pivot. Entry valid.",blocking=False)
    else:
        return GATE_RESULT("pivot_confirm","fail",val_str,f"> ${pivot:.2f}",
            f"Stock has NOT closed above pivot ${pivot:.2f}. Wait for confirmation.",blocking=True)

def _gate_position_size(inputs: dict, best_candidate: dict) -> dict:
    acct_cad  = float(inputs.get("account_size", 24813))
    cad_usd   = float(inputs.get("cad_usd_rate", 0.73))
    risk_pct  = float(inputs.get("risk_pct", 0.01))
    acct_usd  = acct_cad * cad_usd
    max_risk  = acct_usd * risk_pct
    premium   = best_candidate.get("premium_per_lot", 0)
    lots      = int(max_risk // premium) if premium > 0 else 0
    val_str   = f"{lots} lot(s) at 1% risk (${max_risk:.0f} USD)"
    if lots >= 1:
        return GATE_RESULT("position_size","pass",val_str,">= 1 lot","Position size viable.",blocking=False)
    else:
        return GATE_RESULT("position_size","warn",val_str,">= 1 lot",
            f"Premium ${premium:.0f} exceeds 1% risk budget ${max_risk:.0f} USD.",blocking=False)

def run_gates(inputs: dict, chain: dict, candidates: list,
              iv_history: list, direction: str = "buy_call") -> list:
    if not candidates:
        return []
    best = candidates
    selected_dte = best.get("dte", 45)
    inputs["selected_dte"] = selected_dte
    if direction == "buy_call":
        return [
            safe_gate("ivr",           _gate_ivr,           inputs, chain, iv_history),
            safe_gate("hv_iv",         _gate_hv_iv,         inputs, chain, iv_history),
            safe_gate("theta_burn",    _gate_theta_burn,     inputs, best),
            safe_gate("dte",           _gate_dte,            inputs, selected_dte),
            safe_gate("events",        _gate_events,         inputs),
            safe_gate("liquidity",     _gate_liquidity,      chain, best),
            safe_gate("market_regime", _gate_market_regime,  inputs),
            safe_gate("pivot_confirm", _gate_pivot_confirm,  inputs),
            safe_gate("position_size", _gate_position_size,  inputs, best),
        ]
    # Track B (sell_put) — add when needed
    return []

def _get_atm_iv(chain: dict) -> float:
    spot = chain.get("underlying_price", 0)
    opts = [o for o in chain.get("options", []) if o.get("right") == "C" and o.get("implied_vol")]
    if not opts:
        return 0.20
    atm = min(opts, key=lambda o: abs(o["strike"] - spot))
    return atm["implied_vol"]

def _days_to_next_fomc() -> int:
    from datetime import date
    fomc_2026 = [date(2026,1,29),date(2026,3,18),date(2026,5,6),
                 date(2026,6,17),date(2026,7,29),date(2026,9,16),
                 date(2026,11,4),date(2026,12,16)]
    today = date.today()
    future = [d for d in fomc_2026 if d >= today]
    return (future - today).days if future else 999
```


---

## 13. `strategy_ranker.py`

```python
"""
Rank top 3 option strategies from chain data.
Pure computation — no I/O, no external calls.
"""
from datetime import datetime

def rank_strategies(inputs: dict, chain: dict) -> list:
    opts = [o for o in chain.get("options", []) if o.get("right") == "C"
            and o.get("delta") is not None and o.get("implied_vol")]
    if not opts:
        return []
    spot = chain["underlying_price"]
    t1   = float(inputs.get("target1", spot * 1.085))
    t2   = float(inputs.get("target2", spot * 1.185))

    # Select expiry closest to recommended DTE
    rec_dte = int(inputs.get("recommended_dte", 45))
    today = datetime.today()
    expiries = sorted(set(o["expiry"] for o in opts))
    def dte(exp):
        try: return (datetime.strptime(str(exp)[:8], "%Y%m%d") - today).days
        except: return 999
    best_expiry = min(expiries, key=lambda e: abs(dte(e) - rec_dte))
    exp_opts = [o for o in opts if str(o["expiry"])[:8] == str(best_expiry)[:8]]
    if not exp_opts:
        exp_opts = opts

    def closest_delta(target_delta):
        return min(exp_opts, key=lambda o: abs((o.get("delta") or 0) - target_delta))

    # Candidate 1: ITM Call Δ0.68
    c1_opt = closest_delta(0.68)
    c1_prem = (c1_opt.get("ask", 0) + c1_opt.get("bid", 0)) / 2 or c1_opt.get("last", 5.0)
    c1 = _build_candidate(1, "ITM Call — Δ0.68", "itm_call", c1_opt, c1_prem, spot, t1, t2,
        "Highest probability. Intrinsic value shields theta. Best for momentum breakouts.",
        warning=None)

    # Candidate 2: Bull Call Spread (ATM long / T1 short)
    c2_long_opt = closest_delta(0.52)
    c2_short_strike = min(exp_opts, key=lambda o: abs(o["strike"] - t1))
    c2_long_prem  = (c2_long_opt.get("ask",0)+c2_long_opt.get("bid",0))/2 or c2_long_opt.get("last",5.0)
    c2_short_prem = (c2_short_strike.get("bid",0)+c2_short_strike.get("ask",0))/2 or c2_short_strike.get("last",1.5)
    c2_net = max(0.05, c2_long_prem - c2_short_prem)
    c2_max_gain = (c2_short_strike["strike"] - c2_long_opt["strike"] - c2_net) * 100
    c2 = {
        "rank": 2, "label": "Bull Call Spread", "strategy_type": "spread",
        "strike_display": f"${c2_long_opt['strike']:.0f}C / ${c2_short_strike['strike']:.0f}C",
        "expiry_display": _fmt_expiry(best_expiry),
        "dte": dte(best_expiry),
        "premium_per_lot": round(c2_net * 100, 2),
        "breakeven": round(c2_long_opt["strike"] + c2_net, 2),
        "delta": round((c2_long_opt.get("delta",0.52) - c2_short_strike.get("delta",0.24)), 3),
        "theta_per_day": round((c2_long_opt.get("theta",0) - c2_short_strike.get("theta",0)), 4),
        "vega": round((c2_long_opt.get("vega",0) - c2_short_strike.get("vega",0)), 4),
        "gamma": round((c2_long_opt.get("gamma",0) - c2_short_strike.get("gamma",0)), 4),
        "implied_vol": c2_long_opt.get("implied_vol", 0.19),
        "max_gain_per_lot": round(c2_max_gain, 2),
        "max_loss_per_lot": round(c2_net * 100, 2),
        "spread_pct": _spread_pct(c2_long_opt),
        "why": "Lowest cost. Short strike caps at Target 1. Best % return to T1. Low theta burn.",
        "warning": None, "_raw_option": c2_long_opt
    }

    # Candidate 3: ATM Call Δ0.52
    c3_opt = closest_delta(0.52)
    c3_prem = (c3_opt.get("ask",0)+c3_opt.get("bid",0))/2 or c3_opt.get("last",6.0)
    c3 = _build_candidate(3, "ATM Call — Δ0.52", "atm_call", c3_opt, c3_prem, spot, t1, t2,
        "Highest gamma. Best for explosive breakouts only. Fastest theta decay.",
        warning="⚠️ HIGH THETA — only for explosive breakout (>5% gap up)")

    return [c1, c2, c3]

def _build_candidate(rank, label, stype, opt, prem, spot, t1, t2, why, warning):
    return {
        "rank": rank, "label": label, "strategy_type": stype,
        "strike_display": f"${opt['strike']:.0f}C",
        "expiry_display": _fmt_expiry(opt["expiry"]),
        "dte": _dte_from_expiry(opt["expiry"]),
        "premium_per_lot": round(prem * 100, 2),
        "breakeven": round(opt["strike"] + prem, 2),
        "delta": opt.get("delta"), "theta_per_day": opt.get("theta"),
        "vega": opt.get("vega"), "gamma": opt.get("gamma"),
        "implied_vol": opt.get("implied_vol"),
        "max_gain_per_lot": None,
        "max_loss_per_lot": round(prem * 100, 2),
        "spread_pct": _spread_pct(opt),
        "why": why, "warning": warning, "_raw_option": opt
    }

def _fmt_expiry(exp):
    try:
        return datetime.strptime(str(exp)[:8], "%Y%m%d").strftime("%b %Y")
    except: return str(exp)

def _dte_from_expiry(exp):
    try:
        return (datetime.strptime(str(exp)[:8], "%Y%m%d") - datetime.today()).days
    except: return 45

def _spread_pct(opt):
    b, a = opt.get("bid"), opt.get("ask")
    if b and a and b > 0 and a > 0:
        return round((a - b) / ((a + b) / 2) * 100, 1)
    return None
```


---

## 14. `pnl_calculator.py`

```python
"""
P&L per 1 lot (100 shares) at expiry for 6 price scenarios × 3 strategies.
Pure computation — no I/O.
"""
import os

CAD_USD = float(os.getenv("CAD_USD_RATE", 0.73))

def compute_pnl_table(inputs: dict, candidates: list) -> dict:
    spot    = float(inputs.get("entry_momentum") or inputs.get("underlying_price", 234.35))
    stop    = float(inputs.get("stop_loss", spot * 0.92))
    t1      = float(inputs.get("target1",   spot * 1.085))
    t2      = float(inputs.get("target2",   spot * 1.185))
    pivot   = float(inputs.get("vcp_pivot", spot * 1.033))
    acct    = float(inputs.get("account_size", 24813)) * CAD_USD
    risk    = float(inputs.get("risk_pct", 0.01))

    scenarios = [
        {"label": "Stop Loss 🔴",   "price": stop,      "color": "red"},
        {"label": "Sideways / -4%", "price": spot*0.96, "color": "neutral"},
        {"label": "Current Price",  "price": spot,      "color": "neutral"},
        {"label": "VCP Pivot ⚡",   "price": pivot,     "color": "amber"},
        {"label": "Target 1 ✅",    "price": t1,        "color": "green"},
        {"label": "Target 2 🎯",    "price": t2,        "color": "green"},
    ]

    rows = []
    for sc in scenarios:
        p = sc["price"]
        stock_move = (p - spot) / spot * 100
        cols = []
        for c in candidates[:3]:
            pnl = _pnl(c, p)
            pnl_pct = pnl / c["max_loss_per_lot"] * 100 if c["max_loss_per_lot"] > 0 else 0
            cols.append({"pnl": round(pnl, 2), "pnl_pct": round(pnl_pct, 1)})
        rows.append({
            "scenario": sc["label"],
            "price": round(p, 2),
            "stock_move_pct": round(stock_move, 1),
            "color": sc["color"],
            "cols": cols
        })

    footer = {
        "breakevens": [c.get("breakeven") for c in candidates[:3]],
        "theta_burns_7d": [round(abs(c.get("theta_per_day",0)) * 7 * 100, 0) for c in candidates[:3]],
        "max_losses": [c.get("max_loss_per_lot") for c in candidates[:3]],
        "lots_at_1pct": [round((acct * risk) / c["max_loss_per_lot"], 1)
                         if c.get("max_loss_per_lot", 0) > 0 else 0 for c in candidates[:3]]
    }
    return {"rows": rows, "footer": footer}

def _pnl(candidate: dict, price_at_expiry: float) -> float:
    stype = candidate.get("strategy_type")
    prem  = candidate["max_loss_per_lot"] / 100  # premium per share
    raw   = candidate.get("_raw_option", {})
    strike = raw.get("strike", 0)
    if stype in ("itm_call", "atm_call"):
        return (max(0, price_at_expiry - strike) - prem) * 100
    elif stype == "spread":
        long_strike  = raw.get("strike", strike)
        short_strike = candidate.get("short_strike", strike + 20)
        net_prem     = prem
        intrinsic = min(max(0, price_at_expiry - long_strike),
                        short_strike - long_strike)
        return (intrinsic - net_prem) * 100
    elif stype == "sell_put":
        return (prem - max(0, strike - price_at_expiry)) * 100
    return 0.0
```


---

## 15. `app.py` — Flask Routes + Error Handlers

```python
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from dotenv import load_dotenv
import os, logging, traceback
from datetime import datetime

load_dotenv()
from logger_config import setup_logging
setup_logging()

from exceptions import OptionsIQError, ValidationError
from data_service import data_service
from gate_engine import run_gates
from strategy_ranker import rank_strategies
from pnl_calculator import compute_pnl_table
from circuit_breaker import breakers
from cache_manager import cache

app = Flask(__name__)
CORS(app, origins=["http://localhost:3050"])
logger = logging.getLogger("app")

VERSION = "2.1"
PORT    = int(os.getenv("FLASK_PORT", 5051))

# ── Error Handlers ────────────────────────────────────────────────────────────

@app.errorhandler(OptionsIQError)
def handle_optionsiq_error(e: OptionsIQError):
    code = 400 if isinstance(e, ValidationError) else 503
    return jsonify({"error": type(e).__name__, "message": e.message,
                    "recoverable": e.recoverable, "context": e.context,
                    "data_mode": data_service.current_mode()}), code

@app.errorhandler(Exception)
def handle_unexpected(e: Exception):
    logger.exception("Unhandled exception")
    return jsonify({"error": "InternalError", "message": str(e),
                    "trace": traceback.format_exc()[-500:]}), 500

# ── Health ────────────────────────────────────────────────────────────────────

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "version": VERSION,
                    **data_service.health(), "timestamp": datetime.now().isoformat()})

# ── Main Analysis ─────────────────────────────────────────────────────────────

@app.post("/api/options/analyze")
def analyze():
    body = request.get_json(force=True, silent=True) or {}
    ticker    = (body.get("ticker") or "").upper().strip()
    direction = body.get("direction", "buy_call")

    if not ticker:
        from exceptions import ValidationError
        raise ValidationError("ticker", "ticker is required")
    if direction not in ("buy_call", "sell_put", "sell_call", "buy_put"):
        from exceptions import ValidationError
        raise ValidationError("direction", f"Invalid direction: {direction}")

    # Fetch data
    chain      = data_service.get_options_chain(ticker)
    iv_history = data_service.get_historical_iv(ticker)
    spy        = data_service.get_spy_regime()
    body.setdefault("spy_above_200sma",  spy.get("above_200sma", True))
    body.setdefault("spy_5day_return",   spy.get("five_day_return", 0.0))
    body.setdefault("underlying_price",  chain.get("underlying_price", 0))
    body.setdefault("cad_usd_rate", float(os.getenv("CAD_USD_RATE", 0.73)))

    # Rank strategies first (needed for gate 3 theta check)
    candidates = rank_strategies(body, chain)

    # Determine recommended DTE for gate 4
    vcp = float(body.get("vcp_confidence", 0))
    adx = float(body.get("adx", 0))
    rec_dte = 21 if (vcp >= 80 and adx >= 40) else 45 if vcp >= 60 else None
    body["recommended_dte"] = rec_dte

    # Run gates
    gates = run_gates(body, chain, candidates, iv_history, direction)

    # Score
    passed   = sum(1 for g in gates if g["status"] == "pass")
    blocking = next((g for g in gates if g.get("blocking") and g["status"] == "fail"), None)
    total    = len(gates)
    if blocking:
        verdict_status = "fail"
        verdict_color  = "red"
        headline = f"⛔ BLOCKED — {blocking['id'].upper().replace('_',' ')}: {blocking['reason'][:60]}"
    elif any(g["status"] == "fail" for g in gates):
        verdict_status = "fail"
        verdict_color  = "red"
        headline = "FAIL — Critical gate not passed"
    elif any(g["status"] == "warn" for g in gates):
        verdict_status = "warn"
        verdict_color  = "amber"
        headline = "⚠️ CAUTION — Review warnings before trading"
    else:
        verdict_status = "pass"
        verdict_color  = "green"
        headline = "✅ ALL GATES PASS — Entry valid on confirmed close"

    # P&L table
    pnl = compute_pnl_table(body, candidates)

    # Behavioral checks (always 4, always shown)
    pivot  = float(body.get("vcp_pivot", 0))
    close  = float(body.get("last_close", 0))
    behavioral = [
        {"id":"gate8_block","type":"hard_block" if close <= pivot else "info",
         "label": "Gate 8: Pivot Confirmation",
         "message": f"Stock close ${close:.2f} vs pivot ${pivot:.2f}. "
                    f"{'NOT confirmed — wait for close above pivot.' if close <= pivot else 'Confirmed ✓'}"},
        {"id":"entry_rr","type":"warning",
         "label": "Entry Timing",
         "message": "Momentum entry R:R may be lower than pullback entry. "
                    "System preferred entry is pullback. Verify R:R >= 2:1 before committing."},
        {"id":"vrp_headwind","type":"warning",
         "label": "VRP Headwind",
         "message": "All 3 AI peer reviews confirm: IV exceeds realized vol >80% of the time. "
                    "Your stock win rate does NOT guarantee options profitability. Paper trade 60 days minimum."},
        {"id":"lottery_bias","type":"warning",
         "label": "Lottery Bias",
         "message": "Highest % return ≠ best choice. Higher delta (Δ0.68) = higher probability of profit. "
                    "Do not chase the ATM call for its leverage alone."}
    ]

    # IVR data
    current_iv = next(
        (o.get("implied_vol",0) for o in chain.get("options",[])
         if o.get("right")=="C" and abs((o.get("delta") or 0)-0.52) < 0.15), 0.19
    )
    iv_vals = [h["iv"] for h in iv_history if h.get("iv")]
    ivr_pct = round(sum(1 for v in iv_vals if v <= current_iv*100) / len(iv_vals) * 100, 1) if iv_vals else None

    return jsonify({
        "ticker": ticker, "direction": direction,
        "track": "A" if direction in ("buy_call","sell_call") else "B",
        "underlying_price": chain.get("underlying_price"),
        "data_source": chain.get("_source","mock"),
        "ibkr_connected": data_service.ibkr.is_connected(),
        "data_mode": data_service.current_mode(),
        "cache_hit": chain.get("_cache","live"),
        "timestamp": datetime.now().isoformat(),
        "swing_data": {k: body.get(k) for k in [
            "swing_signal","entry_pullback","entry_momentum","stop_loss",
            "target1","target2","risk_reward","vcp_pivot","vcp_confidence",
            "adx","last_close","s1_support","earnings_days_away","pattern"]},
        "verdict": {"status": verdict_status, "color": verdict_color,
                    "gates_passed": passed, "gates_total": total,
                    "score_label": f"{passed}/{total}",
                    "blocking_gate": blocking["id"] if blocking else None,
                    "headline": headline},
        "gates": gates,
        "behavioral_checks": behavioral,
        "top_strategies": [{k:v for k,v in c.items() if not k.startswith("_")}
                           for c in candidates],
        "pnl_table": pnl,
        "ivr_data": {"current_iv": round(current_iv*100,1),
                     "ivr_pct": ivr_pct,
                     "history_days": len(iv_history),
                     "fallback_used": len(iv_history) < 30},
        "recommended_dte": rec_dte,
        "direction_locked": (["sell_call","buy_put"]
                             if body.get("swing_signal")=="BUY" else []),
        "_provenance": {"bid_ask_available": chain.get("bid_ask_available",False),
                        "greeks_source": chain.get("greeks_source","unknown")}
    })

# ── Utility Routes ────────────────────────────────────────────────────────────

@app.get("/api/options/chain/<ticker>")
def get_chain(ticker):
    chain = data_service.get_options_chain(ticker.upper())
    return jsonify(chain)

@app.get("/api/options/ivr/<ticker>")
def get_ivr(ticker):
    hist = data_service.get_historical_iv(ticker.upper())
    return jsonify({"ticker": ticker, "history_days": len(hist),
                    "sample": hist[-5:] if hist else []})

@app.post("/api/options/seed-iv/<ticker>")
def seed_iv(ticker):
    hist = data_service.get_historical_iv(ticker.upper(), days=365)
    return jsonify({"seeded_days": len(hist), "ticker": ticker})

@app.post("/api/options/paper-trade")
def paper_trade():
    from cache_manager import DB_PATH
    import sqlite3
    b = request.get_json(force=True) or {}
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("""INSERT INTO paper_trades
            (ticker,direction,strategy_rank,strike,expiry,premium,lots,account_size,recorded_at)
            VALUES (?,?,?,?,?,?,?,?,?)""",
            (b.get("ticker"), b.get("direction"), b.get("strategy_rank"),
             b.get("strike"), b.get("expiry"), b.get("premium"),
             b.get("lots",1), b.get("account_size",24813),
             datetime.now().isoformat()))
        conn.commit()
    return jsonify({"success": True, "trade_id": cur.lastrowid})

@app.get("/api/options/paper-trades")
def list_paper_trades():
    from cache_manager import DB_PATH
    import sqlite3
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute("SELECT * FROM paper_trades ORDER BY recorded_at DESC").fetchall()
    keys = ["id","ticker","direction","strategy_rank","strike","expiry",
            "premium","lots","account_size","recorded_at","status"]
    return jsonify([dict(zip(keys,r)) for r in rows])

# ── Diagnostic Routes ─────────────────────────────────────────────────────────

@app.get("/api/cache/status")
def cache_status():
    return jsonify(cache.stats())

@app.get("/api/cache/clear")
def cache_clear():
    ticker = request.args.get("ticker")
    dtype  = request.args.get("type")
    cache.invalidate(ticker=ticker, data_type=dtype)
    return jsonify({"cleared": True, "ticker": ticker, "type": dtype})

@app.get("/api/circuit/status")
def circuit_status():
    return jsonify({k: v.status() for k, v in breakers.items()})

@app.post("/api/circuit/reset")
def circuit_reset():
    name = (request.get_json(force=True) or {}).get("name")
    if name in breakers:
        breakers[name].reset()
        return jsonify({"reset": True, "name": name})
    return jsonify({"error": "Unknown breaker", "available": list(breakers.keys())}), 400

@app.get("/api/logs/tail")
def logs_tail():
    n = int(request.args.get("lines", 50))
    try:
        with open("logs/app.log") as f:
            lines = f.readlines()
        return jsonify({"lines": lines[-n:]})
    except FileNotFoundError:
        return jsonify({"lines": []})

# ── Integration Seam ──────────────────────────────────────────────────────────

@app.get("/api/integrate/ping")
def integrate_ping():
    return jsonify({"status":"ok","version":VERSION,"accepts_swing_data":True})

@app.get("/api/integrate/schema")
def integrate_schema():
    return jsonify({"swing_data_fields": {
        "ticker":"str","swing_signal":"BUY|HOLD|AVOID",
        "entry_pullback":"float","entry_momentum":"float","stop_loss":"float",
        "target1":"float","target2":"float","risk_reward":"float",
        "vcp_pivot":"float","vcp_confidence":"float (0-100)","adx":"float",
        "last_close":"float","s1_support":"float","earnings_days_away":"int",
        "pattern":"VCP|Cup&Handle|FlatBase|None",
        "spy_above_200sma":"bool","spy_5day_return":"float"
    }})

@app.get("/api/integrate/status")
def integrate_status():
    swing_url = os.getenv("SWING_ANALYZER_URL","http://localhost:5001")
    try:
        import requests as req
        r = req.get(f"{swing_url}/api/health", timeout=2)
        connected = r.status_code == 200
    except Exception:
        connected = False
    return jsonify({"swing_analyzer_reachable": connected,
                    "swing_url": swing_url})

if __name__ == "__main__":
    logger.info(f"OptionsIQ v{VERSION} starting on port {PORT}")
    app.run(host="0.0.0.0", port=PORT, debug=False, use_reloader=False)
```


---

## 16. Frontend — Key Rules for All Components

```
COLOR VARIABLES (index.css):
  --bg: #0D1117   --bg2: #161B22   --bg3: #1C2333
  --green: #00C896   --red: #FF4444
  --amber: #F59E0B   --blue: #3B82F6   --purple: #A78BFA
  --border: #30363D  --text: #E6EDF3   --text-dim: #8B949E

DIRECTION SELECTOR (DirectionSelector.jsx):
  - Auto-select "buy_call" when swing_signal === "BUY"
  - Disable "sell_call" and "buy_put" with tooltip when swing_signal === "BUY"
  - "sell_put" remains manually selectable on BUY signal

STRATEGY CARDS (TopThreeCards.jsx):
  - ALL 3 cards render with "🔒 GATED OUT" overlay (position:absolute, full-card)
    when verdict.blocking_gate === "pivot_confirm"
  - Overlay removed only when all blocking gates pass

P&L TABLE (PnLTable.jsx):
  - Show "--" in all P&L cells when pivot_confirm gate is "fail"
  - profit cells: color var(--green), font-family monospace
  - loss cells: color var(--red), font-family monospace
  - Target rows: green left-border highlight
  - Candidate 3 column header: "⚠️ HIGH THETA" badge

BEHAVIORAL CHECKS (BehavioralChecks.jsx):
  - Always render all 4 — never hideable, never dismissable
  - Purple left-border accent (#A78BFA)

IBKR STATUS (Header.jsx):
  - Green dot "● IB Gateway LIVE" when ibkr_connected === true
  - Red dot "○ Mock Mode" when ibkr_connected === false
  - Click → alert modal with port instructions

SWING IMPORT STRIP (SwingImportStrip.jsx):
  - Manual mode: all fields editable inline, amber "✎ MANUAL" badge
  - Auto mode (from URL param auto=true): read-only, green "● LIVE" badge

URL PARAM HANDLING (App.jsx):
  - On load: check ?ticker=AME&auto=true
  - If present: auto-call POST /api/options/analyze with ticker
```


---

## 17. Build Order

**Phase 1 — Backend (curl test after each step)**

```
1. exceptions.py
2. logger_config.py
3. circuit_breaker.py
4. cache_manager.py          ← replaces old iv_store cache logic
5. mock_provider.py
6. bs_calculator.py
7. ibkr_provider.py
8. yfinance_provider.py
9. data_service.py           ← wires all providers together
10. gate_engine.py           ← safe_gate wrapper on all gates
11. strategy_ranker.py
12. pnl_calculator.py
13. app.py                   ← all routes + error handlers
TEST: curl -X POST localhost:5051/api/options/analyze \
  -H "Content-Type: application/json" \
  -d '{"ticker":"AME","direction":"buy_call","vcp_pivot":242.05,
       "last_close":234.35,"vcp_confidence":70,"adx":40.2,
       "swing_signal":"BUY","stop_loss":192.93,"target1":254.62,
       "target2":278.36,"spy_above_200sma":true,"account_size":24813}'
```

**Phase 2 — Verify IBKR live data**

```
14. Test: curl localhost:5051/api/options/chain/AME
    → Should return ibkr data, NOT mock
15. Test: curl localhost:5051/api/options/seed-iv/AME
    → Should return seeded_days > 100
16. Test: curl localhost:5051/api/circuit/status
    → All circuits should be CLOSED
```

**Phase 3 — Frontend**

```
17. App.jsx + useOptionsData hook
18. SwingImportStrip + manual form
19. DirectionSelector (4 cards, lock logic)
20. MasterVerdict + GatesGrid
21. BehavioralChecks (4 hardcoded)
22. TopThreeCards (GATED OUT overlay)
23. PnLTable (6 scenarios × 3 strategies)
24. PaperTradeBanner
```

**Phase 4 — Integration Seam**

```
25. Verify /api/integrate/ping returns 200
26. Verify /api/integrate/schema returns field list
27. URL param auto-load works: localhost:3050?ticker=AME&auto=true
```


---

## 18. Test Cases — All Must Pass

| \# | Test | Expected |
| :-- | :-- | :-- |
| TC1 | `last_close=234.35, vcp_pivot=242.05` | Gate 8 FAIL, all 3 cards show GATED OUT |
| TC2 | `last_close=243.00, vcp_pivot=242.05` | Gate 8 PASS, cards visible |
| TC3 | IVR > 50 on buy_call | Gate 1 FAIL blocking=True, verdict=red |
| TC4 | `direction=sell_put` | Track B gates run, no ITM/ATM call shown |
| TC5 | `direction=sell_call, swing_signal=BUY` | Frontend shows locked card |
| TC6 | IB Gateway offline | mock_provider used, header "○ Mock Mode" |
| TC7 | P\&L at stop_loss price | All 3 strategies show -100% loss |
| TC8 | `iv_history` empty | Gate 1 uses absolute IV fallback, no crash |
| TC9 | `account_size=10000, premium=12.00` | Gate 9 WARN, lots_allowed=0 |

<div align="center">⁂</div>

[^1]: Options-Learning-1.docx

[^2]: image.jpg

[^3]: https://www.quantstart.com/articles/Self-Study-Plan-for-Becoming-a-Quantitative-Trader-Part-I/

