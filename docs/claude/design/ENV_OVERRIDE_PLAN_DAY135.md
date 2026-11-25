# Plan (Day 135): stop a stale launch environment from silently beating `.env` (ROADMAP #29)

## Context
Day 133: Alpaca got HTTP 401 for about 4 days. The backend was started from a terminal that still held old Alpaca keys. `load_dotenv(...)` does not override variables already in the environment, so the old keys beat the fixed `.env`. The Alpaca breaker opened and the chain fell through to Twelve Data with no loud sign. A full restart fixed it. Goal: this cannot happen silently again.

## Facts read from the code (Day 135)
- `load_dotenv` is called in 6 places (review: the first draft said 4), each with the default `override=False`: `backend/backend.py:126`, `backend/providers/__init__.py:22`, `backend/backtest/simfin_loader.py:18`, `backend/backtest/audit_data_sources.py:462`, plus `backend/providers/backtest_adapter.py:27` and `backend/backtest/backtest_adx_rsi_thresholds.py:35`. Same rule in 6 copies (Golden Rule 59).
- `.env` holds 11 entries (10 keys plus the `ALPACA_DATA_FEED` setting, which is not a secret) (Twelve Data, Finnhub, FMP, Alpha Vantage, EODHD, Alpaca x3, FRED, SimFin, Tradier). `start.sh` launches `python backend.py` from the user's shell, so the shell's environment is inherited.
- Tests that set env: `test_alpaca_provider.py`, `test_tradier_errors.py` (they set it after import; to confirm in the build step).
- `alpaca_provider.py:120` already prints a 401 line, but nobody reads the log at start-up.

## Approach (recommended)
One helper, one rule: **`.env` wins over the launch environment, and the app says so loudly.**

1. New `backend/env_loader.py` with `load_env(path=None)`:
   - Reads `.env` with `dotenv_values` (no side effects).
   - Finds keys where the process environment already has a different non-empty value. Compares values but prints only the **key names**, never any value or prefix (ENGINEER.md, keys and secrets).
   - Calls `load_dotenv(path, override=True)`.
   - Logs one line per run: `ENV: .env replaced N stale launch-environment value(s): ALPACA_API_KEY, ... (restart your terminal to clear them)`. A missing `.env` also logs a loud line.
   - Runs once per process (module flag), so the 6 callers do not print 6 times.
   - Escape hatch: `STA_ENV_OVERRIDE=0` keeps the old behaviour (environment wins) and logs a warning naming the differing keys instead.
2. Replace all 6 `load_dotenv` calls with `load_env()`. Keep the `ImportError` guard (python-dotenv missing).
3. Show it where the user looks: add the list of overridden key names to the `/api/health` answer (field `envOverridden`, empty list normally). Optional; drop if the review says it widens the blast radius.
4. Docs: `.env.example` comment, KNOWN_ISSUES entry closed, ROADMAP #29 closed, rule text in `rules/data-providers.md` (one sentence), ENGINEER.md miss row.

## Why not only a warning
A warning still leaves the app on the wrong key until a restart, and someone has to read the log. Override fixes the cause and the log line keeps it visible. The cost: a one-off `KEY=x python script.py` is now beaten by `.env`; `STA_ENV_OVERRIDE=0` covers that.

## Blast radius (to confirm in review)
- Every provider key now comes from `.env`. Any key that exists only in the shell (not in `.env`) is untouched, because override only applies to keys present in `.env`.
- Tests that set env **before** importing `providers` would be overridden. Check both test files; use the escape hatch or set env after import if needed.
- `launchd` paper-trading job (`daily_job.py`, discontinued): imports `providers`, so it also gets `.env` values. No change in practice.

## Verification
1. New `backend/test_env_loader.py` (throwaway temp `.env`, `monkeypatch`): stale value overridden; same value not reported; empty env value filled; key absent from `.env` untouched; missing `.env`; escape hatch; log text contains key names and **no value**; runs once. Mutation check: switch `override=True` off and expect failures.
2. Existing suites: `test_alpaca_provider.py`, `test_tradier_errors.py`, `./run_all_checks.sh --quick`.
3. Real check: start the backend with `ALPACA_API_KEY=stale ./start.sh backend`, expect the log line naming `ALPACA_API_KEY`, then one real Alpaca call returns data (not 401). Restart normally afterwards.
4. Grep proves no `load_dotenv(` remains outside the helper.

## Process
Write this to `docs/claude/design/ENV_OVERRIDE_PLAN_DAY135.md`, get an Opus review (Golden Rule 55: it changes a rule with several copies and affects every provider), apply it, build, `/three-pass`, stamp with `--plan`.

## Opus review (Day 135), applied: verdict GO WITH CHANGES
Premises checked against the code. Changes made to this plan:
1. **6 call sites, not 4** (added `providers/backtest_adapter.py:27`, `backtest/backtest_adx_rsi_thresholds.py:35`); the grep check covers all 6.
2. **`test_alpaca_provider.py` would break**: it sets fake keys at lines 13-16, then imports `providers` at line 17, so the override would replace them with real `.env` keys. Fix: set `STA_ENV_OVERRIDE=0` before the import, and confirm the checks at :84 and :139 still pass. `test_tradier_errors.py` is safe (sets the token after import; read when the provider is built).
3. **No `load_dotenv(override=True)`.** The helper writes `os.environ[k] = v` itself, only where the `.env` value is not None and not empty, so a blank `KEY=` line never wipes a good shell key. The "which keys differ" check and the write use the same rule. Test for the blank case.
4. **Test-only reset** `_reset_for_tests()` for the run-once flag.
5. **Log and `/api/health` field: key names only.** No values, lengths, hashes or prefixes; no `verbose=True`. A test searches the log output and the health answer for every test value.
6. Key count corrected; `ALPACA_DATA_FEED` is described as a setting, not a stale key.
Confirmed fine: import-time key reads in `news_engine`, `econ_engine`, `cycles_engine` come after the load in `backend.py`; no launchd plist or script passes keys; `/api/health` (`backend.py:703`) consumers read only `status` and `providers`; python-dotenv 1.0.1.
Override is the right default over warn-only (single-user local app; warn-only would still have left Alpaca on the wrong key for 4 days).
Out of scope, reported to the user: an old FRED key value sits in committed `docs/claude/versioned/archive/KNOWN_ISSUES_DAY62.md:88`.
