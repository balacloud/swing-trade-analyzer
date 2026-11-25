"""Tests for env_loader.load_env (Day 135, plan ENV_OVERRIDE_PLAN_DAY135.md). Throwaway .env files, no real keys.
Run: cd backend && venv/bin/python test_env_loader.py"""
import io, os, sys, tempfile, contextlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import env_loader as el

passed = failed = 0
def ok(cond, name):
    global passed, failed
    if cond: passed += 1
    else:
        failed += 1; print('FAIL', name)

SECRETS = ['old-secret-AAA', 'new-secret-BBB', 'same-secret-CCC', 'fill-secret-DDD', 'keep-secret-EEE']
KEYS = ['T_STALE', 'T_SAME', 'T_FILL', 'T_BLANK', 'T_ONLY_SHELL', 'STA_ENV_OVERRIDE']

def run(env_text, shell, path_name='.env'):
    for k in KEYS: os.environ.pop(k, None)
    os.environ.update(shell)
    d = tempfile.mkdtemp(); p = os.path.join(d, path_name)
    open(p, 'w').write(env_text)
    el._reset_for_tests()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        got = el.load_env(p)
    return got, buf.getvalue(), p

ENV = 'T_STALE=new-secret-BBB\nT_SAME=same-secret-CCC\nT_FILL=fill-secret-DDD\nT_BLANK=\n'
SHELL = {'T_STALE': 'old-secret-AAA', 'T_SAME': 'same-secret-CCC', 'T_BLANK': 'keep-secret-EEE', 'T_ONLY_SHELL': 'x'}

got, out, p = run(ENV, SHELL)
ok(got == ['T_STALE'], 'only the differing key is reported')
ok(os.environ['T_STALE'] == 'new-secret-BBB', '.env replaces a stale launch value')
ok(os.environ['T_SAME'] == 'same-secret-CCC', 'an equal value is left alone')
ok(os.environ['T_FILL'] == 'fill-secret-DDD', 'a missing variable is filled from .env')
ok(os.environ['T_BLANK'] == 'keep-secret-EEE', 'a blank KEY= line never wipes a good value')
ok(os.environ['T_ONLY_SHELL'] == 'x', 'a shell-only key is untouched')
ok('T_STALE' in out and 'T_SAME' not in out and 'T_FILL' not in out, 'log names only the replaced key')
ok(not any(s in out for s in SECRETS), 'log never contains any value')
ok(el.overridden_keys() == ['T_STALE'] and not any(s in ' '.join(el.overridden_keys()) for s in SECRETS), 'health list has names only')

# runs once per path: a second call prints nothing and changes nothing
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    again = el.load_env(p)
ok(again == ['T_STALE'] and buf.getvalue() == '', 'second call is silent and returns the same list')

# escape hatch: environment wins, loud warning, names only
got, out, _ = run(ENV, dict(SHELL, STA_ENV_OVERRIDE='0'))
ok(os.environ['T_STALE'] == 'old-secret-AAA', 'STA_ENV_OVERRIDE=0 keeps the launch value')
ok(got == ['T_STALE'] and 'T_STALE' in out and 'STA_ENV_OVERRIDE=0' in out, 'escape hatch warns with the key name')
ok(not any(s in out for s in SECRETS), 'escape hatch log never contains any value')

# the reloader child sees no difference itself but still reports the names the parent replaced
got, out, p = run(ENV, SHELL)                      # parent process replaces T_STALE
el._done.clear()                                   # a fresh process: nothing recorded locally, env var inherited
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    child = el.load_env(p)
ok(child == [] and el.overridden_keys() == ['T_STALE'], 'child process still reports the replaced key names')
ok(os.environ.get('STA_ENV_OVERRIDDEN') == 'T_STALE', 'only key names are passed to the child')

# nothing differs: silent
got, out, _ = run('T_SAME=same-secret-CCC\n', {'T_SAME': 'same-secret-CCC'})
ok(got == [] and out == '', 'no difference: no output')

# edge cases a real .env can hold: bare key, comment-only file, quoted value, spaces around =, relative path form
got, out, p = run('# only a comment\nT_BLANK\nT_STALE = "new-secret-BBB"\n', {'T_STALE': 'old-secret-AAA', 'T_BLANK': 'keep-secret-EEE'})
ok(got == ['T_STALE'] and os.environ['T_STALE'] == 'new-secret-BBB', 'quoted value with spaces around = is read the same way dotenv reads it')
ok(os.environ['T_BLANK'] == 'keep-secret-EEE', 'a bare KEY line (no =) never wipes a value')
cwd = os.getcwd(); os.chdir(os.path.dirname(p))
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    again = el.load_env(os.path.basename(p))
os.chdir(cwd)
ok(buf.getvalue() == '' and again == ['T_STALE'], 'the same file by a relative path is not loaded twice')
got, out, _ = run('# nothing here\n', {'T_STALE': 'old-secret-AAA'})
ok(got == [] and out == '' and os.environ['T_STALE'] == 'old-secret-AAA', 'comment-only .env changes nothing and prints nothing')
got, out, _ = run('T_STALE=new-secret-BBB\n', {'T_STALE': '   '})
ok(os.environ['T_STALE'] == 'new-secret-BBB' and not any(s in out for s in SECRETS), 'a whitespace-only launch value is replaced, log shows no value')

# missing .env: loud line, no crash
for k in KEYS: os.environ.pop(k, None)
el._reset_for_tests()
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    got = el.load_env(os.path.join(tempfile.mkdtemp(), 'nope.env'))
ok(got == [] and 'not found' in buf.getvalue(), 'missing .env is reported')

# the real .env of this checkout loads without printing any value
el._reset_for_tests()
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    el.load_env()
real_values = [v for v in __import__('dotenv').dotenv_values(el._DEFAULT_ENV).values() if v and len(v) >= 6]
ok(not any(v in buf.getvalue() for v in real_values), 'real .env: no value appears in the log')

el._reset_for_tests()
print(f'{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
