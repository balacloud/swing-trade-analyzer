"""One place that loads backend/.env (Day 135, plan docs/claude/design/ENV_OVERRIDE_PLAN_DAY135.md, ROADMAP #29).

Why: python-dotenv's default never replaces a variable that is already in the environment. Day 133: the backend was
started from a terminal holding old Alpaca keys, those won over the fixed .env, Alpaca returned 401 for about 4 days and
the chain fell through to Twelve Data with no loud sign.

Rule: a non-empty value in .env WINS over the launch environment, and the app says which KEY NAMES were replaced.
- A blank `KEY=` line in .env never wipes a value that is already set.
- Key names only are ever printed: never a value, length, hash or prefix (ENGINEER.md, keys and secrets).
- Escape hatch: STA_ENV_OVERRIDE=0 in the launch environment keeps the old behaviour (environment wins) and only warns.
- Flask's debug reloader runs the app in a CHILD process that inherits the already-fixed environment, so the child would
  see no difference. The parent therefore passes the replaced key NAMES to the child in STA_ENV_OVERRIDDEN.
- Runs once per .env path per process, so the several importers do not print the line several times.
"""
import os

_DEFAULT_ENV = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
_PASSED = 'STA_ENV_OVERRIDDEN'
_done = {}   # abs path -> list of key names that differed


def _passed_names():
    return [n for n in os.environ.get(_PASSED, '').split(',') if n]


def load_env(path=None):
    """Load .env into os.environ. Returns the sorted key names whose launch-environment value differed from .env."""
    path = os.path.realpath(path or _DEFAULT_ENV)
    if path in _done:
        return list(_done[path])
    try:
        from dotenv import dotenv_values
    except ImportError:
        print("⚠️ ENV: python-dotenv not installed - API keys must be set in the environment")
        _done[path] = []
        return []
    if not os.path.isfile(path):
        print(f"⚠️ ENV: {path} not found - API keys must be set in the environment")
        _done[path] = []
        return []

    keep_env = os.environ.get('STA_ENV_OVERRIDE', '1').strip() == '0'
    differ = []
    for key, value in dotenv_values(path).items():
        if value is None or value == '':
            continue                       # bare or blank line: never wipe a good value
        current = os.environ.get(key)
        if current is None or current == '':
            os.environ[key] = value        # nothing to replace: just fill it
        elif current != value:
            differ.append(key)
            if not keep_env:
                os.environ[key] = value
    differ.sort()
    if differ and keep_env:
        print(f"🛑 ENV: STA_ENV_OVERRIDE=0, so {len(differ)} launch-environment value(s) beat .env: {', '.join(differ)}. "
              f"These providers may use old keys.")
    elif differ:
        print(f"🛑 ENV: .env replaced {len(differ)} stale launch-environment value(s): {', '.join(differ)}. "
              f"Restart your terminal to clear them.")
    _done[path] = differ
    if differ and not keep_env:
        os.environ[_PASSED] = ','.join(sorted(set(differ) | set(_passed_names())))   # names only, for the reloader child
    return list(differ)


def overridden_keys():
    """Key names (never values) that differed between the launch environment and .env, for /api/health."""
    out = set(_passed_names())
    for names in _done.values():
        out.update(names)
    return sorted(out)


def _reset_for_tests():
    _done.clear()
    os.environ.pop(_PASSED, None)
