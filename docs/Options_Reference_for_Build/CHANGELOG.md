# Changelog

## 2026-03-05

### Added
- `chain_profile` support for options-chain retrieval:
  - `smart` (default): one expiry, min DTE constrained, targeted strikes/contracts.
  - `full`: broader expiry/strike/contract scope.
- Profile-aware chain cache keys (`ticker + profile + direction`) to prevent smart/full cache collisions.
- Profile-specific timeout controls:
  - `ANALYZE_TIMEOUT_SMART_SEC`
  - `ANALYZE_TIMEOUT_FULL_SEC`
- New analyze response fields:
  - `chain_profile`
  - `min_dte`
  - `chain_quality`
- `GET /api/options/chain/<ticker>` query controls:
  - `chain_profile`
  - `min_dte`
  - `direction`
  - `target_price`

### Changed
- Backend moved to an intelligent pull model (targeted contracts) instead of broad chain retrieval by default.
- `smart` profile now selects the nearest expiry at or above `min_dte` (default `14`).
- Analyze/cache/refresh paths now pass profile context for consistent retrieval behavior.
- `.env` reorganized into smart/full profile knobs.

### Fixed
- NaN normalization in IB option fields (`openInterest`, quotes, greeks, etc.) to avoid parse/runtime crashes.
- `StrategyRanker` now safely handles missing numeric fields (no 500 on `None` greeks/delta).
- Client ID collision resilience improved by scanning fallback IDs when primary is in use.
- Partial fallback now respects `chain_profile` behavior (smart fallback is one-expiry/min-DTE filtered).

### Known Issues
- Full live IB chain success still depends on IB latency/entitlements; requests may degrade to `ibkr_partial`.
- Under sustained IB slowness, smart/full paths can still hit timeout and trigger fallback.
