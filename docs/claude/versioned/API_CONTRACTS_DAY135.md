# API Contracts — Day 135

> Changes since `API_CONTRACTS_DAY129.md`. Backend v2.58 → v2.59. Plan: `docs/claude/design/ENV_OVERRIDE_PLAN_DAY135.md`.

## Changed — `GET /api/health`
- New field **`env_overridden`**: sorted list of environment variable NAMES (never values) where `backend/.env` replaced a different launch-environment value. Normally `[]`. Existing fields unchanged; consumers read only `status` and `providers`.
