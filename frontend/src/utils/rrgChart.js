/**
 * rrgChart — pure layout for the Sectors-tab RRG chart (Day 126).
 * x = RS-Ratio (100-centred), y = RS-Momentum (0-centred, STA convention; the
 * standard chart's 100 line is our 0 line). Each sector has a `tail` of its last
 * few weekly points. No React here so it can be unit-tested.
 */

export const RRG_COLORS = {
  Leading: '#22c55e', Improving: '#3b82f6', Weakening: '#eab308', Lagging: '#ef4444',
};

const isNum = (v) => typeof v === 'number' && Number.isFinite(v);

/** Sectors with a usable current point. Bad tail points are dropped, not guessed. */
function usable(sectors) {
  return (sectors || []).filter((s) => s && isNum(s.rsRatio) && isNum(s.rsMomentum));
}

/**
 * @returns {{w,h,plot,cx,cy,hx,hy,points:Array}}
 * points[i] = {etf, quadrant, x, y, tail:[{x,y}], labelY}
 */
export function buildRrgModel(sectors, { w = 640, h = 420 } = {}) {
  const pad = { l: 44, r: 16, t: 16, b: 34 };
  const plot = { l: pad.l, t: pad.t, r: w - pad.r, b: h - pad.b };
  const pw = plot.r - plot.l;
  const ph = plot.b - plot.t;
  const list = usable(sectors);

  // Symmetric domain around (100, 0) so the cross is always in the middle.
  let maxDx = 0;
  let maxDy = 0;
  list.forEach((s) => {
    maxDx = Math.max(maxDx, Math.abs(s.rsRatio - 100));
    maxDy = Math.max(maxDy, Math.abs(s.rsMomentum));
    (Array.isArray(s.tail) ? s.tail : []).forEach((t) => {
      if (t && isNum(t.rs_ratio) && isNum(t.rs_momentum)) {
        maxDx = Math.max(maxDx, Math.abs(t.rs_ratio - 100));
        maxDy = Math.max(maxDy, Math.abs(t.rs_momentum));
      }
    });
  });
  const hx = Math.max(1.5, +(maxDx * 1.15).toFixed(2));
  const hy = Math.max(1.5, +(maxDy * 1.15).toFixed(2));

  const toX = (ratio) => plot.l + ((ratio - 100 + hx) / (2 * hx)) * pw;
  const toY = (mom) => plot.t + ((hy - mom) / (2 * hy)) * ph;

  const points = list.map((s) => ({
    etf: s.etf,
    quadrant: s.quadrant,
    x: toX(s.rsRatio),
    y: toY(s.rsMomentum),
    tail: (Array.isArray(s.tail) ? s.tail : [])
      .filter((t) => t && isNum(t.rs_ratio) && isNum(t.rs_momentum))
      .map((t) => ({ x: toX(t.rs_ratio), y: toY(t.rs_momentum) })),
    labelY: 0,
  }));

  // Label de-overlap: walk top to bottom, push a label down if it sits within
  // 12px of an earlier label that is horizontally close.
  const order = [...points].sort((a, b) => a.y - b.y);
  const placed = [];
  order.forEach((p) => {
    let ly = p.y + 4;
    placed.forEach((q) => {
      if (Math.abs(q.x - p.x) < 36 && Math.abs(q.labelY - ly) < 12) ly = q.labelY + 12;
    });
    p.labelY = Math.min(ly, plot.b - 2);
    placed.push(p);
  });

  return { w, h, plot, cx: toX(100), cy: toY(0), hx, hy, points };
}
