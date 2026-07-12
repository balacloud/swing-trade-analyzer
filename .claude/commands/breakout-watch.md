# Breakout Watch — EOD Breakout State Sweep

Report which watchlist stocks broke out today, using STA's 8-state breakout
classification engine (`backend/breakout_detection.py`, behind
`/api/breakout/<ticker>` and `/api/breakout/batch`). This is an on-demand,
read-only sweep — no push notifications, no cron, no auto-trading
(`docs/claude/design/BREAKOUT_ENHANCEMENT_PLAN.md` Phase 3).

**Naming note:** the engine has a literal state called `BREAKOUT_WATCH` —
this skill reports across all 8 states, not just that one. Don't imply
otherwise in the report header (e.g. don't say "showing BREAKOUT_WATCH
tickers" when you mean "running the breakout-watch sweep").

## Step 1: Determine the ticker list

1. If tickers were passed as arguments (space- or comma-separated), use
   those (uppercase them).
2. Else use Nirmal's watchlist — the same 20 tickers as the Scan tab's
   preset (`NIRMAL_WATCHLIST` const in `frontend/src/App.jsx`):
   `SMCI, NVDA, AAPL, MSFT, GOOGL, AMZN, AMD, TSLA, PLTR, ORCL, CRM, MU,
   MARA, JNJ, JPM, VZ, TXN, HOOD, COP, PYPL`
3. If neither applies (no args, and the user hasn't indicated they want the
   default watchlist), ask which tickers to check rather than guessing.

## Step 2: Check the backend is running

`curl -sf http://localhost:5001/api/health`. If it fails, tell the user the
backend isn't running and offer to run `./start.sh` from the project root
before continuing. **Do not proceed without a live backend response** —
never fabricate breakout states from memory or a prior run.

## Step 3: Fetch breakout states

- If the ticker list has ≤20 tickers: one call to `POST /api/breakout/batch`
  with body `{"tickers": [...]}` (Day 81, Breakout Enhancement Plan Task 2.1 —
  this is the batch endpoint built for the Scan tab's badge column, reused
  here for the same reason: one request instead of N).
- If >20 tickers: split into batches of 20 (the endpoint hard-caps at 20
  per request) and combine the results.
- Per-ticker failures come back as `{"error": ...}` entries *within* the
  batch response, not as a failed HTTP request — treat those as "couldn't
  check X", not as `NOT_READY`.

## Step 4: Bucket and report, most actionable first

1. **Confirmed breakouts** (`BREAKOUT_CONFIRMED`) — ticker, RVOL, humanAction text
2. **Retest entries** (`RETEST_ENTRY`)
3. **Watch** (`BREAKOUT_WATCH`)
4. **Warnings** (`SUPPLY_WARNING`, `FAILED_BREAKOUT`, `EXTENDED_CHASE_RISK`) —
   surface these prominently; they are risk flags, not opportunities
5. **Building base** (`BUILDING_BASE`)
6. Everything `NOT_READY`: one summary line ("N others: not ready"), not
   itemized per ticker

For every ticker reported in buckets 1–5, append the engine's own
`humanAction` text **verbatim** — do not paraphrase it into a stronger
claim. **Never state a `BREAKOUT_CONFIRMED` result as a buy
recommendation** — this is a hard rule from
`docs/claude/design/BREAKOUT_ENGINE_SPEC.md` §13/§15, not a style choice.
Report state, not signal.

Tickers that errored (no data / fetch failure) get their own short line
("couldn't check: X, Y — [reason]"), kept separate from the `NOT_READY`
summary line.

## Step 5: Suggest one follow-up

End with a single suggestion like "Run full analysis on TICKER for more
detail" pointing at the 1–2 most interesting candidates (confirmed/retest/
watch) — not a prompt to analyze the whole list.

## Rules

- This is a different, faster modality than the screenshot-based chart
  review workflow (`prompts/STA_CLAUDE_CHART_REVIEW_PROMPT.md`) — this
  sweep is API-driven across many tickers at once; that workflow is a
  deeper, chart-visual review of one ticker. Don't conflate the two when
  explaining what this does.
- No intraday/real-time alerting — this is an on-demand, EOD-quality
  snapshot only, whenever it's run.
- Never fabricate a status if an API call fails — report the failure,
  don't guess or reuse a stale value.
- This skill only classifies and reports breakout state. It does not
  place orders, does not modify the frozen paper-trading config, and does
  not touch verdict/scoring logic.
