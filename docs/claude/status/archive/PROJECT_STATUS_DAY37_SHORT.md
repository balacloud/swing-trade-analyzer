# Project Status - Day 37 (Short)

> **Date:** January 26, 2026
> **Version:** v3.6 (Backend v2.9)
> **Focus:** SQLite Persistent Cache + Architecture Cleanup

---

## Session Summary

### What Was Accomplished Today

1. **SQLite Persistent Cache** - Major infrastructure upgrade
   - Created `cache_manager.py` (400 lines) with intelligent TTL
   - OHLCV cache: Expires at next market close (4pm ET + 30min buffer)
   - Fundamentals cache: 7-day TTL (quarterly data)
   - **Survives restarts** - no more lost cache on backend restart
   - Performance: 5.5x faster on cache hits (1.9s → 0.3s)

2. **Backend v2.9** - Upgraded with SQLite integration
   - New cache endpoints: `/api/cache/status`, `/api/cache/clear`
   - Hit rate tracking and cache statistics
   - Market-aware expiry (no pointless refreshes at 2am)

3. **Utility Scripts** - Developer convenience
   - `start.sh` - Start backend/frontend/both
   - `stop.sh` - Stop services cleanly

4. **Documentation Cleanup**
   - Moved obsolete files to `docs/obsolete/`
   - Reviewed Perplexity research docs (kept with caveats)

5. **Architecture Decisions**
   - Confirmed local calculations (SMA, EMA, RSI, ATR) use industry-standard formulas
   - TradingView Phase 2: Will use free Lightweight Charts library (no subscription)

---

## Current State

| Component | Status | Notes |
|-----------|--------|-------|
| Backend | v2.9 | SQLite cache integrated |
| Frontend | v3.5 | Stable |
| SQLite Cache | WORKING | 124KB, survives restarts |
| OHLCV Cache | WORKING | Market-aware TTL |
| Fundamentals Cache | WORKING | 7-day TTL |
| TradingView Widget | Phase 1 | Free iframe (RSI/MACD) |

---

## Pending Tasks (Next Session)

| Priority | Task | Effort | Notes |
|----------|------|--------|-------|
| 1 | **Lightweight Charts (Phase 2)** | Medium | Show our S&R levels on chart |
| 2 | Forward Testing UI | High | Trade journal + R-multiple |
| 3 | Cache warming script | Low | Pre-populate cache for watchlist |

---

## Key Decisions Made

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Cache storage | SQLite | Persistent, survives restarts |
| OHLCV TTL | Market-aware | No refresh until next close |
| Fundamentals TTL | 7 days | Quarterly data |
| TradingView Phase 2 | Lightweight Charts | Free, open source |
| S&R method | Keep agglomerative | Validated 100% detection |

---

## Files Changed This Session

```
backend/cache_manager.py              (NEW - 400 lines)
backend/data/cache.db                 (NEW - auto-created)
backend/backend.py                    (MODIFIED - v2.9)
start.sh                              (NEW)
stop.sh                               (NEW)
docs/obsolete/                        (NEW - moved legacy files)
docs/claude/status/PROJECT_STATUS_DAY37_SHORT.md  (NEW)
docs/claude/versioned/KNOWN_ISSUES_DAY37.md       (NEW)
```

---

## Cache Performance Summary

| Request Type | First (Miss) | Second (Hit) | Speedup |
|-------------|--------------|--------------|---------|
| `/api/stock/AAPL` | ~1.0s | ~0.5s | 2x |
| `/api/fundamentals/AAPL` | ~1.9s | ~0.3s | **5.5x** |

---

## Golden Rule Reminder

> **"Cache intelligently, not blindly."**
>
> Market-aware TTL means OHLCV data expires at the next market close,
> not after an arbitrary 24 hours. No point refreshing at 2am when
> markets are closed.

---

*Reference: CLAUDE_CONTEXT.md for full project context*
