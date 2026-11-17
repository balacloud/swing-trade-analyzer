/**
 * One money format for every price on the Analyze page (Day 126, Statement Audit).
 * Before this, the header used toLocaleString (half-up, thousands commas) while the Technical Read, pullback plan and MR rows used toFixed(2)
 * (binary rounding, no commas): RIVN at $12.045 read "$12.05" in the header and "$12.04" in the Entry block; a $1,234.56 stock read
 * "$1,234.56" in one place and "$1234.56" in another. Everything now goes through here.
 * Non-finite input returns the dash, never "NaN".
 */
export function formatMoney(v, dash = '—') {
  return typeof v === 'number' && Number.isFinite(v)
    ? `$${v.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`
    : dash;
}
