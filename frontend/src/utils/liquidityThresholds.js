/**
 * Shared cap-aware liquidity thresholds
 *
 * Day 70B: cap-aware tiers replaced a flat $10M rule (multi-LLM audit found
 * flat $10M was misleading for small/mid caps — a $10M/day small-cap is
 * plenty liquid for swing size, a $10M/day large-cap is thin).
 *
 * Day 83: extracted from simplifiedScoring.js into a shared module — Quality
 * Gates (scoringEngine.js) and the Analyze page's Price Card (App.jsx) each
 * had their own separate, and inconsistent, liquidity standard (a flat $10M
 * gate and a flat $10M/$50M color split respectively). This is now the one
 * place the tiers live; the same stock's liquidity assessment can no longer
 * disagree depending which view is open.
 */
export function getLiquidityThreshold(marketCap) {
  if (marketCap >= 10e9) return { threshold: 10e6, label: '$10M', capLabel: 'large-cap' };
  if (marketCap >= 2e9) return { threshold: 5e6, label: '$5M', capLabel: 'mid-cap' };
  return { threshold: 2e6, label: '$2M', capLabel: 'small-cap' };
}
