/**
 * Price Structure Narrative Generator
 * Day 72 — Phase 1 implementation
 *
 * Generates structured price narrative from existing S/R + pattern data.
 * No new backend computation — reads data already returned by fetchFullAnalysisData().
 *
 * Architecture: Frontend utility (follows categoricalAssessment.js pattern).
 * All inputs come from fetchFullAnalysisData() result — no extra API calls.
 *
 * Required backend change: sr.meta.levelScores (1 line, backend.py Day 72).
 *
 * Design spec: docs/claude/design/PRICE_STRUCTURE_CARD_SPEC.md (v2)
 * Audit report: docs/claude/design/PRICE_STRUCTURE_CARD_AUDIT.md
 */

// Volume threshold — same constant as pattern_detection.py check_breakout_quality()
const BREAKOUT_VOLUME_THRESHOLD = 1.5;

/**
 * Is price "near" a level? ATR-relative proximity.
 * "Near" = within 2x ATR (the noise range). Not an arbitrary percentage.
 */
function isNearLevel(currentPrice, level, atr) {
  if (!level || !atr || atr <= 0) return false;
  return Math.abs(currentPrice - level) <= 2.0 * atr;
}

/**
 * Get touch count for a specific price level from the levelScores map.
 * levelScores keys are stringified rounded prices e.g. "689.28".
 */
function getTouches(level, levelScores) {
  if (!levelScores || !level) return null;
  const key = String(Math.round(level * 100) / 100);
  // Also try with varying decimal precision
  for (const k of Object.keys(levelScores)) {
    if (Math.abs(parseFloat(k) - level) < 0.5) {
      return levelScores[k];
    }
  }
  return null;
}

/**
 * Is this level confluent on both daily + weekly timeframes?
 */
function isConfluent(level, confluenceMap) {
  if (!confluenceMap || !level) return false;
  for (const k of Object.keys(confluenceMap)) {
    if (Math.abs(parseFloat(k) - level) < 0.5) {
      return confluenceMap[k]?.confluent === true;
    }
  }
  return false;
}

/**
 * Compute distance % from current price to a level.
 * Positive = above current price (resistance), negative = below (support).
 */
function distancePct(currentPrice, level) {
  if (!level || !currentPrice) return null;
  return ((level - currentPrice) / currentPrice) * 100;
}

/**
 * Derive structure state from Trend Template score + ATR-relative proximity.
 * 12-rule priority-ordered decision tree. Edge cases evaluated first.
 */
function deriveStructureState(currentPrice, resistance, support, trendCriteria, adx, atr) {
  const R1 = resistance?.[0];
  const S1 = support?.[0];
  const tt = trendCriteria ?? 0;
  const adxVal = adx?.adx ?? 0;

  // Rule 1: No levels at all
  if (!R1 && !S1) return { state: 'Insufficient data', color: 'gray', rule: 1 };

  // Rule 2: ATH breakout — no resistance above price
  if (!R1 && S1) return { state: 'ATH breakout — blue sky', color: 'green', rule: 2 };

  // Rule 3: Below all support
  if (R1 && !S1) return { state: 'Below all support', color: 'red', rule: 3 };

  // Rule 4: Compression — near both R1 and S1
  if (isNearLevel(currentPrice, R1, atr) && isNearLevel(currentPrice, S1, atr)) {
    return { state: 'Compression — range narrowing', color: 'yellow', rule: 4 };
  }

  // Rules 5-7: Strong uptrend (TT >= 7)
  if (tt >= 7) {
    if (isNearLevel(currentPrice, R1, atr)) return { state: 'Uptrend testing resistance', color: 'green', rule: 5 };
    if (isNearLevel(currentPrice, S1, atr)) return { state: 'Uptrend pulling back to support', color: 'green', rule: 6 };
    return { state: 'Uptrend — between levels', color: 'green', rule: 7 };
  }

  // Rules 8-10: Mixed trend (TT 4-6)
  if (tt >= 4) {
    if (isNearLevel(currentPrice, S1, atr)) return { state: 'Weakening trend — testing support', color: 'yellow', rule: 8 };
    if (isNearLevel(currentPrice, R1, atr)) return { state: 'Transitioning — testing resistance', color: 'yellow', rule: 9 };
    return { state: 'Mixed trend — between levels', color: 'yellow', rule: 10 };
  }

  // Rules 11-12: Weak / no trend (TT < 4)
  if (adxVal < 15) return { state: 'Choppy — no clear trend', color: 'red', rule: 11 };
  return { state: 'Downtrend', color: 'red', rule: 12 };
}

/**
 * Build the key levels array — nearest first, max 2R + 2S.
 * Each level includes type, price, touches, confluent, distancePct.
 */
function buildKeyLevels(currentPrice, resistance, support, levelScores, confluenceMap) {
  const levels = [];

  const addLevels = (prices, type) => {
    const nearest = (prices || []).slice(0, 2);
    for (const price of nearest) {
      const dist = distancePct(currentPrice, price);
      levels.push({
        type,
        price,
        touches: getTouches(price, levelScores),
        confluent: isConfluent(price, confluenceMap),
        distancePct: dist != null ? Math.abs(dist).toFixed(1) : null,
        above: type === 'resistance',
      });
    }
  };

  addLevels(resistance, 'resistance');
  addLevels(support, 'support');

  return levels;
}

/**
 * Generate up to 3 watch items — the highest-value section.
 * Priority-ordered: compression > near resistance > near support > extended > pattern > fallback.
 */
function generateWatchItems(currentPrice, resistance, support, atr, rvol, rsiDaily, tradeViability, patterns, levelScores) {
  const items = [];
  const R1 = resistance?.[0];
  const S1 = support?.[0];
  const r1Touches = getTouches(R1, levelScores);
  const s1Touches = getTouches(S1, levelScores);
  const r1Dist = R1 ? Math.abs(distancePct(currentPrice, R1)).toFixed(1) : null;
  const s1Dist = S1 ? Math.abs(distancePct(currentPrice, S1)).toFixed(1) : null;

  // Priority 1: Compression
  if (R1 && S1 && isNearLevel(currentPrice, R1, atr) && isNearLevel(currentPrice, S1, atr)) {
    const rangePct = (((R1 - S1) / currentPrice) * 100).toFixed(1);
    items.push(`Tight range between S1–R1 (${rangePct}%) — directional resolution expected`);
  }

  // Priority 2: Near resistance
  if (R1 && isNearLevel(currentPrice, R1, atr)) {
    const touchStr = r1Touches ? `, tested ${r1Touches}x` : '';
    if (rvol >= BREAKOUT_VOLUME_THRESHOLD) {
      items.push(`Breakout watch: near R1 ($${R1.toFixed(2)}${touchStr}) — volume confirming (${rvol}x avg)`);
    } else {
      items.push(`Approaching R1 ($${R1.toFixed(2)}${touchStr}) — needs volume > ${BREAKOUT_VOLUME_THRESHOLD}x for conviction (current: ${rvol}x)`);
    }
  }

  // Priority 3: Near support
  if (S1 && isNearLevel(currentPrice, S1, atr)) {
    const touchStr = s1Touches ? `, held ${s1Touches}x` : '';
    if (rsiDaily != null && rsiDaily < 30) {
      items.push(`Testing S1 ($${S1.toFixed(2)}${touchStr}) with RSI oversold (${rsiDaily.toFixed(0)}) — watch for bounce`);
    } else if (rsiDaily != null && rsiDaily < 40) {
      items.push(`Testing S1 ($${S1.toFixed(2)}${touchStr}) — RSI approaching oversold (${rsiDaily.toFixed(0)})`);
    } else {
      items.push(`Drifting toward S1 ($${S1.toFixed(2)}${touchStr}) — break below invalidates setup`);
    }
  }

  // Priority 4: Extended from support
  const viable = tradeViability?.viable;
  const supportDist = tradeViability?.support_distance_pct;
  if (viable === 'NO' && supportDist > 15) {
    items.push(`Extended ${supportDist.toFixed(0)}% from support — pullback entry preferred over chase`);
  }

  // Priority 5: Actionable pattern convergence
  const actionable = (patterns?.actionablePatterns || []).filter(p => p.confidence >= 60);
  if (actionable.length > 0) {
    const best = actionable[0];
    const pivot = best.triggerPrice ? ` — pivot at $${parseFloat(best.triggerPrice).toFixed(2)}` : '';
    items.push(`${best.name} forming (${best.confidence}%)${pivot}`);
  }

  // Fallback: Mid-range, nothing imminent
  if (items.length === 0) {
    const parts = [];
    if (R1 && r1Dist) parts.push(`R1 $${R1.toFixed(2)} (${r1Dist}% above)`);
    if (S1 && s1Dist) parts.push(`S1 $${S1.toFixed(2)} (${s1Dist}% below)`);
    items.push(`Between levels — no immediate trigger. ${parts.join(', ')}`);
  }

  return items.slice(0, 3);
}

/**
 * Main public function.
 * Call after fetchFullAnalysisData() resolves.
 *
 * @param {object} sr     - srData from state (fetchSupportResistance result)
 * @param {object} patterns - patternsData from state (fetchPatterns result)
 * @returns {object|null}  - null if insufficient data (card won't render)
 */
export function generatePriceStructure(sr, patterns) {
  if (!sr) return null;

  const currentPrice = sr.currentPrice;
  const resistance = sr.resistance || [];
  const support = sr.support || [];
  const meta = sr.meta || {};
  const atr = meta.atr || 0;
  const rvol = meta.rvol || 1.0;
  const rsiDaily = meta.rsi_daily ?? null;
  const adx = meta.adx || {};
  const tradeViability = meta.tradeViability || {};
  const levelScores = meta.levelScores || {};
  const confluenceMap = meta.mtf?.confluence_map || {};
  const resistanceProjected = meta.resistanceProjected || false;
  const supportProjected = meta.supportProjected || false;

  // Need at least one level to render
  if (resistance.length === 0 && support.length === 0) return null;

  const trendTemplate = patterns?.trendTemplate || {};
  const trendCriteria = trendTemplate.criteria_met ?? null;

  // Handle ATH / ATL projection cases
  let effectiveResistance = resistance;
  let effectiveSupport = support;
  if (resistanceProjected && resistance.length === 0) effectiveResistance = [];
  if (supportProjected && support.length === 0) effectiveSupport = [];

  // Derive structure state
  const { state: structureState, color: stateColor } = deriveStructureState(
    currentPrice, effectiveResistance, effectiveSupport, trendCriteria, adx, atr
  );

  // Build trend context line
  const ttStr = trendCriteria != null ? `${trendCriteria}/8 Minervini` : 'N/A';
  const adxStr = adx.adx != null ? `ADX ${adx.adx} (${adx.trend_strength || ''})` : '';
  const trendContext = [ttStr, adxStr].filter(Boolean).join(' | ');

  // Build key levels
  const keyLevels = buildKeyLevels(currentPrice, effectiveResistance, effectiveSupport, levelScores, confluenceMap);

  // Generate watch items
  const watchItems = generateWatchItems(
    currentPrice, effectiveResistance, effectiveSupport,
    atr, rvol, rsiDaily, tradeViability, patterns, levelScores
  );

  return {
    structureState,
    stateColor,   // 'green' | 'yellow' | 'red' | 'gray'
    trendContext,
    keyLevels,    // [{type, price, touches, confluent, distancePct, above}]
    watchItems,   // string[]
    meta: {
      trendTemplateCriteria: trendCriteria,
      adx: adx.adx,
      rsi: rsiDaily,
      rvol,
      atr,
      levelsUsed: keyLevels.length,
      patternsActive: (patterns?.actionablePatterns || [])
        .filter(p => p.confidence >= 60)
        .map(p => p.name),
    },
  };
}
