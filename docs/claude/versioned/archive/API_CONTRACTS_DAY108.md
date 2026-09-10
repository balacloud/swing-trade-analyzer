# API Contracts — Day 108 (August 14, 2026)

> Adds one query parameter to one existing endpoint. Every endpoint documented in
> prior `API_CONTRACTS_DAY*.md` files (latest: Day 105) is otherwise unchanged.

---

## Changed — `GET /api/context/<ticker>`

### What changed
New optional query parameter `skip_news` (default `false`, fully backward-compatible).

### Why
Found during the Day 107/108 full-system audit (Group 6b, Context tab): this route
always internally called `get_news_endpoint(ticker)`, unconditionally consuming an
Alpha Vantage news credit — even when the frontend's `ContextTab.jsx` called it with
a placeholder `'SPY'` ticker just to get cycles/econ/regime data (no ticker selected
yet), and even when a real ticker was already selected and the frontend's separate
`loadNews(ticker)` call was about to fetch the same news independently a moment
later. `ContextTab.jsx` now always passes `skip_news=true` and relies solely on its
own `loadNews()` for news data.

### Request

```
GET /api/context/<ticker>?skip_news=true
```

`skip_news` accepts `"true"`/`"false"` (case-insensitive string match), defaults to
`false` if omitted — any caller relying on the old always-bundled-news behavior is
unaffected.

### Response shape (unchanged except `news`)

```json
{
  "ticker": "AAPL",
  "overall_regime": "NEUTRAL",
  "regime_counts": {"favorable": 4, "neutral": 3, "adverse": 3},
  "total_indicators": 10,
  "options_block": {"has_options_block": false, "reason": null},
  "cycles": { "...": "unchanged" },
  "econ": { "...": "unchanged" },
  "news": null
}
```

When `skip_news=true`, `news` is `null` instead of the full news-sentiment object.
When omitted or `false`, behavior is identical to before this change.
