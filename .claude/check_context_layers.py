#!/usr/bin/env python3
"""Fast check that the layered docs are complete (run by /sta-end; not a hook).
- Golden Rules: the rule numbers in the GOLDEN_RULES.md index must equal the numbers in
  stable/rules/*.md, each exactly once; rules 1-15 and the always-read rules stay in GOLDEN_RULES.md.
- Reports L1 size so growth is visible.
Exit 1 on any problem."""
import re, glob, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'claude')
gr = open(os.path.join(D, 'stable', 'GOLDEN_RULES.md')).read()
idx = [int(m) for m in re.findall(r'^- \*\*(\d+)\.\*\*', gr, re.M)]
files = []
for f in sorted(glob.glob(os.path.join(D, 'stable', 'rules', '*.md'))):
    files += [int(m) for m in re.findall(r'^(\d+)\. \*\*', open(f).read(), re.M)]
full = [int(m) for m in re.findall(r'^(\d+)\. \*\*', gr, re.M)]
bad = []
if len(idx) != len(set(idx)): bad.append('index lists a rule twice')
if len(files) != len(set(files)): bad.append('a rule appears twice in rules/*.md')
if set(idx) != set(files): bad.append(f'index vs files differ: {sorted(set(idx) ^ set(files))}')
allnums = set(idx) | set(n for n in full if n not in idx)
miss = [n for n in range(1, 70) if n != 27 and n not in allnums]
if miss: bad.append(f'rules with no home: {miss}')
for h in ('ROADMAP_HISTORY', 'PERSONA_LOG', 'ENGINEER_LOG', 'CLAUDE_CONTEXT_LOG', 'KNOWN_ISSUES_LOW_AND_RESOLVED'):
    if not os.path.exists(os.path.join(D, 'history', h + '.md')): bad.append('missing history/' + h + '.md')
l1 = ['CLAUDE_CONTEXT.md', 'stable/GOLDEN_RULES.md', 'stable/PERSONA.md', 'stable/ENGINEER.md', 'stable/ROADMAP.md']
tot = sum(os.path.getsize(os.path.join(D, p)) for p in l1)
print(f'rules indexed: {len(idx)}, in rules files: {len(files)}; L1 core files: {tot/1024:.1f} KB (status + known issues extra)')
if tot > 85 * 1024: bad.append('L1 core over 85 KB: move something to history/')
for b in bad: print('PROBLEM:', b)
sys.exit(1 if bad else 0)
