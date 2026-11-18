#!/usr/bin/env python3
"""Statement Audit summary (Day 127). Usage: venv/bin/python audit_summary.py OUT_DIR [PREVIOUS_OUT_DIR]
Reads OUT_DIR/REPORT.md, REPORT_CARDS.md, REPORT_CARDS2.md, prints one line per report, lists every WRONG row, and (with a previous folder)
the WRONG rows that are NEW since then. Writes OUT_DIR/SUMMARY.txt. Exit code 1 when any WRONG row exists."""
import os, re, sys

REPORTS = ('REPORT.md', 'REPORT_CARDS.md', 'REPORT_CARDS2.md')

def rows(folder):
    out = {}
    for name in REPORTS:
        p = os.path.join(folder, name)
        if not os.path.exists(p):
            continue
        for line in open(p, encoding='utf-8'):
            c = [x.strip() for x in line.split('|')]
            if len(c) > 8 and c[6] in ('WRONG', 'MISLEADING', 'UNVERIFIED', 'PASS'):
                out.setdefault(name, []).append((c[1], c[2], c[3], c[4], c[5], c[6], c[7]))   # ticker, id, claim, shown, recomputed, verdict, severity
    return out

def counts(rs):
    n = {'PASS': 0, 'WRONG': 0, 'MISLEADING': 0, 'UNVERIFIED': 0}
    for r in rs: n[r[5]] += 1
    return n

def main():
    out = sys.argv[1]
    prev = sys.argv[2] if len(sys.argv) > 2 else None
    cur, old = rows(out), (rows(prev) if prev else {})
    lines = [f'Statement audit summary: {out}']
    wrong = []
    for name in REPORTS:
        rs = cur.get(name, [])
        n = counts(rs)
        lines.append(f'  {name:18} PASS {n["PASS"]:5} WRONG {n["WRONG"]:3} MISLEADING {n["MISLEADING"]:3} UNVERIFIED {n["UNVERIFIED"]:4}' + ('' if rs else '   (missing)'))
        wrong += [(name,) + r for r in rs if r[5] == 'WRONG']
    old_keys = {(name, r[0], r[1]) for name, rs in old.items() for r in rs if r[5] == 'WRONG'}
    new = [w for w in wrong if (w[0], w[1], w[2]) not in old_keys] if prev else wrong
    lines.append(f'WRONG rows: {len(wrong)}' + (f' ({len(new)} new since {os.path.basename(prev.rstrip("/"))})' if prev else ''))
    for w in (new if prev else wrong)[:40]:
        lines.append(f'  {w[1]:10} {w[2]:12} {w[3][:60]} | shown "{w[4][:40]}" vs "{w[5][:40]}"')
    text = '\n'.join(lines)
    open(os.path.join(out, 'SUMMARY.txt'), 'w').write(text + '\n')
    print(text)
    return 1 if wrong else 0

if __name__ == '__main__':
    sys.exit(main())
