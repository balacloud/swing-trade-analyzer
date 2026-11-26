/**
 * Data notes under the Analyze header price (Day 135, plan DATA_NOTES_PLAN_DAY135.md).
 * Input: /api/stock `dataNotes` = { integrity: {level, note, bars, since} | null, tracking: {reference, multiple, basis, twin, corr, beta, n, date} | null }.
 * integrity: the Data Sources tab's OWN integrity wording (same builder, backend data_quality.cached_quality), shown only when it is WARN or FAIL.
 * tracking: the audit's measured comparison of a leveraged fund with its underlying. Facts only: no verdict words, no "follows" claim. Correlation is shown
 * with 3 decimals and beta with 2 exactly as stored (rounding 0.995 to "1.00" would read as perfect). Pure, never throws; anything missing is skipped.
 */
function dayLabel(iso, withYear) {
  if (typeof iso !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(iso)) return null;
  const d = new Date(`${iso}T12:00:00`);
  if (Number.isNaN(d.getTime())) return null;
  return d.toLocaleDateString('en-US', withYear ? { month: 'short', day: 'numeric', year: 'numeric' } : { month: 'short', day: 'numeric' });
}

export function describeDataNotes(dn) {
  const out = [];
  try {
    if (!dn || typeof dn !== 'object') return out;
    const i = dn.integrity;
    if (i && (i.level === 'WARN' || i.level === 'FAIL') && typeof i.note === 'string' && i.note) {
      const since = dayLabel(i.since, true);
      const cover = Number.isFinite(i.bars) && since ? ` (of ${i.bars} saved bars since ${since})` : '';
      out.push({ id: 'integrity', level: i.level, text: `Price data: ${i.note}${cover}.` });
    }
    const t = dn.tracking;
    if (t && typeof t.reference === 'string' && t.reference && Number.isFinite(t.corr) && Number.isFinite(t.beta) && Number.isFinite(t.n)) {
      const m = Number.isFinite(t.multiple) ? t.multiple : null;
      let who;
      if (m == null) who = `${t.reference} (multiple not known)`;
      else if (t.twin) who = `${t.reference}, a fund with the same leverage (x${m})`;
      else if (t.basis === 'measured') who = `${t.reference}, the closest match by price (x${m} stated)`;
      else who = `${t.reference} (x${m} stated)`;
      const when = dayLabel(t.date, false);
      out.push({ id: 'tracking', level: 'INFO', text: `Compared with ${who}: correlation ${t.corr.toFixed(3)}, beta ${t.beta.toFixed(2)} over ${t.n} trading days${when ? ` (audit, ${when})` : ''}.` });
    }
  } catch (e) {
    return [];
  }
  return out;
}
