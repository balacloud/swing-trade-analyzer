# Project Status — Day 73 (April 20-21, 2026)

## Version: v4.33 (Backend v2.34, Frontend v4.33, Backtest v4.17, API Service v2.10)

## Session Focus: Nirmal Recovery + Research + Priority Reorder + Value Investing Idea

### What Was Done

**1. Recovered previous session's uncommitted Nirmal work**
- Committed 5 files that were untracked (previous session closed without committing):
  - `backend/backtest/nirmal_validation.py` — validation script
  - `docs/research/nirmal_validation_results.csv` — 378 rows raw data
  - `docs/research/NIRMAL_STA_VALIDATION_RESULTS.md` — full results + interpretation
  - `docs/research/NIRMAL_STA_INTEGRATION_OPPORTUNITIES.md` — 4 gap analysis
  - `docs/research/NIRMAL'S COMPLETE TRADING SYSTEM - CONSO.md` — annotated source

**2. Nirmal Validation Results**
- 378 calls scored: BUY 15.3%, HOLD 40.2%, AVOID 44.4%
- Key finding: Style difference, NOT system failure
- STA = universal quant framework (momentum arm + MR arm + quality + regime)
- Nirmal = multi-style (momentum + value recovery + gap-fill + news catalyst)
- 4 integration gaps identified (N1-N4). N1+N2 approved, N3 deferred, N4 needs validation.

**3. Corrected "Pure Minervini" characterization**
- User caught inaccurate description — STA evolved to universal quant framework (Day 69-70)
- Trend Template survived because it IS standard quant trend definition, not Minervini-specific
- MR arm (RSI(2), Connors) is completely non-Minervini
- Fixed in: memory, NIRMAL_STA_INTEGRATION_OPPORTUNITIES.md, NIRMAL_STA_VALIDATION_RESULTS.md

**4. Regime Awareness — clarity established**
- VIX level alone is lagging and single-dimension
- Full regime = VIX direction + SPY structure (lower highs) + sector rotation + breadth
- April 2026 tariff crash: VIX went 15→18→25→38. STA blind until VIX>30. Nirmal adapted at VIX=18.
- Nirmal's 5-phase framework (Bull Rally/Profit Taking/Rotation/Consolidation/Correction) is the right model
- N4 Market Phase synthesis identified as highest-leverage feature

**5. Priority Reorder (Quant/Trader lens)**

| # | Item | Rationale |
|---|------|-----------|
| 1 | Gate 5: Combined momentum+MR backtest | Quant discipline before paper trading both arms |
| 2 | Behavioral test: Price Structure card | Prerequisite before paper trading use |
| 3 | Paper trading | PRIMARY FOCUS after 1+2 clear |
| 4 | Research + validate N4: Market Phase synthesis | Highest leverage — regime changes every signal |
| 5 | Build N4 | After validation |
| 6-8 | N1, N2, Flip default | Approved quick wins |
| 9 | N3: Gap-fill detection | Deferred post paper trading |
| 10 | Canadian Analyze page | High complexity, medium bug |

**6. Value Investing Tab — idea documented**
- Buffett/Damodaran/Graham/Lynch/Greenblatt style quality-at-fair-price lens
- Separate tab, zero STA swing verdict impact, reuses existing data pipeline
- Minimal new additions: Graham Number, DCF Lite, PEG, FCF Yield, quality checklist
- Documented in ROADMAP.md as planned feature

**7. Value Investing Research Prompts — created**
- `docs/research/VALUE_INVESTING_RESEARCH_PROMPT.md` — 4 prompts for 4 LLMs
  - Prompt 1 (Perplexity): Metric validation against primary sources
  - Prompt 2 (ChatGPT): Cap-size adjustments (small/mid/large)
  - Prompt 3 (Claude Opus): Data availability reality check (yfinance/Finnhub/AlphaVantage)
  - Prompt 4 (Gemini): Failure modes and value traps
- Research must complete before any implementation (Golden Rule #15)

**8. Roadmap + CLAUDE_CONTEXT updated**
- Roadmap: Active Priority Order table, Nirmal Integration section, Value Investing tab, Day 72-73 log, research completed index
- CLAUDE_CONTEXT: Day 73 summary updated, priorities reordered

### Files Created (6)
| File | Purpose |
|------|---------|
| `backend/backtest/nirmal_validation.py` | Nirmal vs STA validation script |
| `docs/research/nirmal_validation_results.csv` | 378-row raw validation data |
| `docs/research/NIRMAL_STA_VALIDATION_RESULTS.md` | Full results + interpretation |
| `docs/research/NIRMAL_STA_INTEGRATION_OPPORTUNITIES.md` | 4 gap analysis + priorities |
| `docs/research/NIRMAL'S COMPLETE TRADING SYSTEM - CONSO.md` | Annotated source doc |
| `docs/research/VALUE_INVESTING_RESEARCH_PROMPT.md` | 4 LLM research prompts |

### Files Modified (4)
| File | Change |
|------|--------|
| `docs/claude/stable/ROADMAP.md` | Active priority order, Nirmal section, Value tab, Day log |
| `docs/claude/CLAUDE_CONTEXT.md` | Day 73 summary, reordered priorities |
| `docs/research/NIRMAL_STA_INTEGRATION_OPPORTUNITIES.md` | Fixed "pure Minervini" → universal quant framework |
| `docs/research/NIRMAL_STA_VALIDATION_RESULTS.md` | Fixed interpretation section |

### Key Decisions
1. **STA is universal quant framework, not Minervini.** Trend Template survived audit as standard trend definition. MR arm is Connors. Don't say "Minervini" in system descriptions.
2. **Regime awareness ≠ just VIX level.** VIX direction + sector rotation + breadth. N4 is highest leverage feature.
3. **Priority reordered:** Gate 5 → behavioral test → paper trading → N4 research → N4 build.
4. **Value Tab goes to research first.** 4 prompts ready. Run next session before any implementation.

### Next Priorities (for Day 74)
1. **Run VALUE_INVESTING_RESEARCH_PROMPT.md** on 4 LLMs (Perplexity, ChatGPT, Claude Opus, Gemini)
2. Bring responses back → synthesize → Value Tab spec
3. Then: Gate 5 combined momentum+MR backtest
