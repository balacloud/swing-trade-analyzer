# Project Status — Day 95 (July 24, 2026)

## Version: v4.51 (Backend v2.44, Frontend v4.46, Backtest v4.19, API Service v2.11) — unchanged

---

## What Happened Today

Short session: paper-trading monitoring, a user question about run-time dependencies (repo/servers), and a real scheduling bug found and fixed in the automated paper-trading job — independent of the freeze (pure ops/config, zero contact with the verdict engine or ledger data).

### 1. Paper trading — monitoring only, no logic changes
Ran `daily_job.py --report`. Momentum: 14 open / 1 closed (unchanged from Day 94). MR: 3 open / 23 closed (unchanged from Day 94). Last job run at check time: 2026-07-22.

### 2. User asked whether the repo/editor or the frontend+backend servers need to be running for the paper-trading job to fire
Answer, confirmed by reading the launchd plist and grepping `daily_job.py`/`live_signals.py`: no. The job is a standalone macOS `launchd` LaunchAgent that runs `daily_job.py` directly — it talks straight to data providers and the SQLite ledger, no calls to `localhost`/the Flask backend. Only requirement: the Mac must be powered on and not asleep at the scheduled fire time.

### 3. Real bug found and fixed: launchd plist assumed the wrong system timezone
User asked "is it CST or EST" about the 16:30 fire time. Checking `/etc/localtime` found this machine's actual local timezone is **America/Toronto (Eastern)**, not Central as the plist's own comment claimed ("16:30 Central Time (this machine's local timezone)"). Since `launchd`'s `StartCalendarInterval` Hour/Minute fields are interpreted in the machine's real local timezone, the job had actually been firing at **4:30pm ET**, not 4:30pm CT — shrinking the intended ~90-minute post-close settling buffer (chosen so daily bars settle across the TwelveData/yfinance/Stooq chain) down to only ~30 minutes, without anyone noticing.

**Fixed:** `~/Library/LaunchAgents/com.sta.papertrading.daily.plist` — all 5 weekday `StartCalendarInterval` entries shifted Hour 16→17 (17:30 ET), comment corrected to state the real timezone and point at this fix. Reloaded via `launchctl unload`/`load`; `launchctl list` confirms the job is registered and healthy. Takes effect starting tomorrow (today's 16:30 window had already passed when this was found).

While investigating, also confirmed (via `job_runs` table, not just the log tail) that the job has in fact been running with real activity every day through 2026-07-22 — an initial read of a truncated log tail looked like it had stalled since 07-15, but the full ledger table showed real `activated`/`closed`/`queued` counts every weekday. Noted, not further chased: the launchd-only log (`daily_job.log`) shows several recent days as "already ran today — skipping," meaning those days' real work likely came from a manual/force run rather than the schedule itself — worth knowing but not investigated further since data currency isn't in question.

**New Golden Rule 33**: verify a scheduled job's actual system timezone before trusting a comment's assumption about it.

---

## Files Changed

| File | Change |
|---|---|
| `~/Library/LaunchAgents/com.sta.papertrading.daily.plist` | Schedule shifted 16:30→17:30 ET (5 weekday entries); comment corrected from wrong "Central Time" assumption to actual Eastern/Toronto; reloaded via launchctl |
| `docs/claude/stable/GOLDEN_RULES.md` | New Rule 33 (verify scheduled-job timezone assumptions) |

**No API changes, no version bump** — config/ops fix only, no `backend.py`/frontend code touched.

---

## All Gates Status

Unchanged from Day 88 onward — no trading-logic, threshold, or verdict changes. Today's plist fix is scheduling/ops only.

**Freeze status:** unchanged — forward-testing accumulation remains the sole active priority. Today's fix was independent of the freeze (same framing as Days 93-94), not an exception to it.

---

## Paper Trading Status (end of session)

- **Momentum:** 14 open, 1 closed. 1/100 toward the confirmation bar. Unchanged from Day 94.
- **MR:** 3 open, 23 closed. 23/100 toward the confirmation bar. Unchanged from Day 94.
- Scheduled fire time corrected to 17:30 ET starting tomorrow — no change to today's already-passed run.

---

## Next Session Priorities

1. **Let paper trading accumulate — still SOLE FOCUS.** Do not propose other roadmap/backlog work unless the user raises it first.
2. Confirm the corrected 17:30 ET schedule actually fires as expected on the next weekday (sanity-check `job_runs`/`daily_job.log` once, not a recurring task).
3. Everything parked at Day 92-94 remains parked: fundamentals mitigation decision, SimFin key rotation, N3, Value Tab Phase 2, volume-confirmation gap (ROADMAP Priority #11), `/ibkr-scan`, Session 28 audit's remaining lower-priority findings (ROADMAP Priority #10).
