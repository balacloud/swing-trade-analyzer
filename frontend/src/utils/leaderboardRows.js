/**
 * leaderboardRows — pure row model for the Sectors-tab leaderboard (Day 126).
 * One row per sector/theme: strength bar centred on 100, momentum arrow, a 5-week
 * line, the corner name, and "moved" when the corner changed a week ago.
 * Corners always come from the backend (item.quadrant, tail[i].quadrant); the cut
 * rule is NOT repeated here (Golden Rule 59).
 */

export const BAR_SCALE = 6; // bar covers 100 +/- 6 RS-Ratio points

const isNum = (v) => typeof v === 'number' && Number.isFinite(v);

/** Points for a small line; returns null when there are fewer than 2 usable values. */
export function sparkPoints(values, w = 92, h = 30, pad = 4) {
  const xs = (values || []).filter(isNum);
  if (xs.length < 2) return null;
  let lo = Math.min(...xs);
  let hi = Math.max(...xs);
  if (hi - lo < 0.8) { // a nearly flat week should look flat, not dramatic
    const mid = (hi + lo) / 2;
    lo = mid - 0.4;
    hi = mid + 0.4;
  }
  return xs.map((v, i) => [
    pad + (i * (w - 2 * pad)) / (xs.length - 1),
    h - pad - ((v - lo) / (hi - lo)) * (h - 2 * pad),
  ]);
}

/**
 * @param items [{key,name,etf,quadrant,rsRatio,rsMomentum,tail?,weekChange?,monthChange?,note?,onScan?}]
 * @returns rows sorted strongest first, each with: bar {side,pct}, spark (points|null),
 *          tail (valid points), prevCorner, moved
 */
export function buildLeaderboardRows(items) {
  return (items || [])
    .filter((i) => i && i.quadrant && isNum(i.rsRatio) && isNum(i.rsMomentum))
    .map((i) => {
      const dev = Math.max(-BAR_SCALE, Math.min(BAR_SCALE, i.rsRatio - 100));
      const tail = (Array.isArray(i.tail) ? i.tail : []).filter(
        (t) => t && isNum(t.rs_ratio) && isNum(t.rs_momentum),
      );
      const prev = tail.length >= 2 ? tail[tail.length - 2] : null;
      const prevCorner = prev && prev.quadrant ? prev.quadrant : null;
      return {
        ...i,
        bar: { side: dev >= 0 ? 'right' : 'left', pct: (Math.abs(dev) / BAR_SCALE) * 50 },
        tail,
        spark: sparkPoints(tail.map((t) => t.rs_ratio)),
        prevCorner,
        moved: !!prevCorner && prevCorner !== i.quadrant,
      };
    })
    .sort((a, b) => b.rsRatio - a.rsRatio);
}
