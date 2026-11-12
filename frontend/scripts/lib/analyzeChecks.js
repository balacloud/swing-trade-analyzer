/**
 * Analyze page checks (Analyze Redesign Step 8, Day 124).
 * Plan: docs/claude/design/ANALYZE_REDESIGN_STEP8_PLAN_DAY124.md (Fable-reviewed).
 *
 * Pure: runChecks(dom, api, helpers) -> [{ id, name, pass, expected, actual }].
 *   dom     - what the browser runner extracted (see ui-verify-checklist.js extractDom)
 *   api     - { spy, qqq, vix, stock, earnings }, each { status, body } as the PAGE
 *             received it (captured from its own network responses); status null
 *             means the response was never seen
 *   helpers - { describeMarketBackdrop, fmtPct, fmtDate } from src/utils/marketBackdrop.js,
 *             passed in so expected text is built by the same code the card uses (GR59)
 * Never throws; a missing input fails its check, it never passes by default.
 */

const CHECK_IDS = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A8', 'A9'];
const NAMES = {
  A1: 'Card order (backdrop first)',
  A2: 'Removed elements absent',
  A3: 'Market backdrop matches API',
  A4: 'Classification line',
  A5: 'Earnings badge and wording',
  A6: 'No blank cards',
  A8: 'Simple view badge',
  A9: 'Cards fit at 390px',
};
const ORDER = ['card-market-backdrop', 'card-stock-header', 'card-technical-read', 'card-mr-read', 'card-trade-setup', 'card-fundamentals', 'card-breakout'];
// A6 measures each card's BODY: the text below its title row and subtitle, which carry
// data-card-head in the app (Fable code review #1: those alone are ~40-130 chars, so a
// whole-card length test passed even when the body was empty).
const MIN_BODY_TEXT = 20;
// A card folded closed by design (data-collapsed="true"; Price Structure was the example until Day 125;
// no card folds today, the branch is kept for future folded cards) shows only
// its header; that header must still carry a status word beyond the title.
const MIN_COLLAPSED_TEXT = 20;
const norm = (s) => String(s ?? '').replace(/\s+/g, ' ').trim();
const ok = (r) => r && r.status === 200 && r.body != null;

function result(id, pass, expected, actual) {
  return { id, name: NAMES[id], pass: !!pass, expected, actual };
}

// Mirrors api.js fetch wrappers: what the page hands describeMarketBackdrop.
function pageInputs(api) {
  const spy = ok(api.spy) ? api.spy.body : null;
  const qqq = ok(api.qqq) ? api.qqq.body
    : api.qqq && api.qqq.status != null ? { error: (api.qqq.body && api.qqq.body.error) || `HTTP ${api.qqq.status}` }
      : null;
  const vix = ok(api.vix) ? { current: api.vix.body.current, regime: api.vix.body.regime } : { current: null, regime: 'unknown' };
  return { spy, qqq, vix };
}

function expectLine(line, fmtPct) {
  return line.state === 'ok' ? `${line.above ? '↑ above' : '↓ below'} ${fmtPct(line.pct)}` : 'not enough history';
}
function expectDrop(drop, fmtDate) {
  if (drop.state === 'no_down_day') return 'no down day in the last 10 sessions';
  if (drop.state !== 'drop') return 'not enough history';
  const suffix = drop.since ? ` (largest since ${fmtDate(drop.since, true)})`
    : drop.searchedFrom ? ` (largest in data back to ${fmtDate(drop.searchedFrom, true)})` : '';
  return `${drop.pct.toFixed(1)}% on ${fmtDate(drop.date)}${suffix}`;
}

function checkA1(dom) {
  const ids = (dom.cards || []).map(c => c.id);
  const idx = ORDER.map(id => ids.indexOf(id));
  const missing = ORDER.filter((id, i) => idx[i] < 0);
  const inOrder = missing.length === 0 && idx.every((v, i) => i === 0 || v > idx[i - 1]);
  const first = ids[0] === 'card-market-backdrop';
  return result('A1', first && inOrder, ORDER.join(' → '),
    missing.length ? `missing: ${missing.join(', ')}` : ids.join(' → ') || 'no cards');
}

function checkA2(dom) {
  const found = [];
  // shortTexts: [{ text, card }] for every short leaf element. The Trade Setup's
  // price-bar label "BUY $338.70" is the buy price, not a verdict, so that one is allowed.
  // Known blind spot (Fable code review #5): a regressed "BUY" verdict badge placed
  // inside the Trade Setup card would pass; HOLD/AVOID anywhere, or BUY elsewhere, fail.
  const shorts = (dom.shortTexts || []).map(x => ({ text: norm(x && x.text), card: x && x.card }));
  const isPriceLabel = (x) => x.card === 'card-trade-setup' && x.text === 'BUY';
  if (shorts.some(x => /^(BUY|HOLD|AVOID)$/.test(x.text) && !isPriceLabel(x))) found.push('BUY/HOLD/AVOID badge');
  if (shorts.some(x => /^[TFSR]:[A-Z]$/.test(x.text))) found.push('T:/F:/S:/R: chips');
  const full = norm(dom.fullText);
  if (full.includes('Holding Period')) found.push('"Holding Period"');
  if (full.includes('Position Size:')) found.push('"Position Size:" banner');
  if (/\bVIABLE\b/.test(full)) found.push('VIABLE badge');
  if (full.includes('Stock not recommended')) found.push('"Stock not recommended"');
  const backdrop = (dom.cards || []).find(c => c.id === 'card-market-backdrop');
  if (backdrop && /\b(Favorable|Unfavorable|Neutral)\b/.test(backdrop.text)) found.push('Favorable/Neutral/Unfavorable label');
  const haveInput = Array.isArray(dom.shortTexts) && typeof dom.fullText === 'string' && !!backdrop;
  return result('A2', haveInput && found.length === 0, 'none of the removed elements',
    !haveInput ? 'page text not extracted' : found.length ? `found: ${found.join(', ')}` : 'none found');
}

function checkA3(dom, api, h) {
  if (!api.spy || api.spy.status == null) return result('A3', false, 'SPY payload', 'SPY response not captured');
  if (!api.qqq || api.qqq.status == null) return result('A3', false, 'QQQ payload', 'QQQ response not captured');
  if (!api.vix || api.vix.status == null) return result('A3', false, 'VIX payload', 'VIX response not captured');
  const exp = h.describeMarketBackdrop(pageInputs(api));
  const rows = (dom.backdrop && dom.backdrop.rows) || [];
  const diffs = [];
  if (rows.length !== exp.rows.length) diffs.push(`rows: expected ${exp.rows.length}, got ${rows.length}`);
  for (const er of exp.rows) {
    const ur = rows.find(r => r.label === er.label);
    if (!ur) { diffs.push(`${er.label}: row missing`); continue; }
    if (er.state !== 'ok') {
      if (!/couldn't load/.test(norm(ur.unavailable))) diffs.push(`${er.label}: expected "couldn't load", got "${norm(ur.unavailable) || norm(ur.long)}"`);
      continue;
    }
    const want = { long: expectLine(er.longTerm, h.fmtPct), short: expectLine(er.shortTerm, h.fmtPct), drop: expectDrop(er.drop, h.fmtDate) };
    for (const k of ['long', 'short', 'drop']) {
      if (norm(ur[k]) !== want[k]) diffs.push(`${er.label} ${k}: expected "${want[k]}", got "${norm(ur[k])}"`);
    }
  }
  const wantVix = exp.vix.state === 'ok'
    ? `VIX ${exp.vix.value.toFixed(1)}${exp.vix.label ? ` · ${exp.vix.label}` : ''} (latest quote)`
    : "VIX: couldn't load";
  const gotVix = norm(dom.backdrop && dom.backdrop.vix);
  if (gotVix !== wantVix) diffs.push(`VIX: expected "${wantVix}", got "${gotVix}"`);
  return result('A3', diffs.length === 0, 'every backdrop figure equals the payload the page received',
    diffs.length ? diffs.join('; ') : `${rows.length} rows + VIX match`);
}

function checkA4(dom, api) {
  if (!ok(api.stock)) return result('A4', false, 'stock payload', 'stock response not captured');
  const header = norm(dom.header);
  if (!header) return result('A4', false, 'header text', 'header not found');
  const etf = api.stock.body.quoteType === 'ETF';
  const bad = header.includes('Unknown');
  const etfOk = !etf || header.includes('Exchange-traded fund (ETF)');
  return result('A4', !bad && etfOk,
    etf ? 'ETF → "Exchange-traded fund (ETF)", never "Unknown"' : 'no "Unknown"',
    bad ? 'header says "Unknown"' : !etfOk ? 'ETF without ETF wording' : 'ok');
}

function checkA5(dom, api) {
  if (!api.earnings || api.earnings.status == null) return result('A5', false, 'earnings payload', 'earnings response not captured');
  const hasUpcoming = ok(api.earnings) ? api.earnings.body.has_upcoming : null;
  const unknown = hasUpcoming === null || hasUpcoming === undefined;
  const fund = (dom.cards || []).find(c => c.id === 'card-fundamentals');
  if (!fund) return result('A5', false, 'Fundamentals card', 'Fundamentals card not found');
  const saysCouldnt = norm(fund.text).includes("Couldn't check the earnings calendar.");
  const wantBadge = hasUpcoming === true;
  const problems = [];
  if (!!dom.earningsBadge !== wantBadge) problems.push(`badge ${dom.earningsBadge ? 'shown' : 'hidden'}, has_upcoming=${hasUpcoming}`);
  if (unknown !== saysCouldnt) problems.push(unknown ? 'feed failed but card does not say so' : 'feed OK but card says it couldn\'t check');
  return result('A5', problems.length === 0,
    unknown ? 'no badge; "Couldn\'t check the earnings calendar."' : wantBadge ? 'badge shown' : 'no badge',
    problems.join('; ') || 'ok');
}

function checkA6(dom) {
  const cards = dom.cards || [];
  const blank = cards.filter(c => {
    if (c.collapsed) return norm(c.text).length < MIN_COLLAPSED_TEXT;
    if (typeof c.bodyText !== 'string') return true; // body not measured: fail, never pass by default
    return norm(c.bodyText).length < MIN_BODY_TEXT;
  }).map(c => c.id);
  return result('A6', cards.length > 0 && blank.length === 0,
    `every open card has a body (≥${MIN_BODY_TEXT} chars below its title); a folded card shows a status word`,
    cards.length === 0 ? 'no cards found' : blank.length ? `blank: ${blank.join(', ')}` : `${cards.length} cards have content`);
}

function checkA8(dom) {
  const t = norm(dom.simpleBadge);
  if (!t) return result('A8', false, '"✅ TRADE" or "⏸️ No Trade" with N/9', 'Simple badge not found');
  const m = t.match(/^(✅ TRADE|⏸️ No Trade)\s*(\d+)\/(\d+) criteria met$/u);
  let pass = !!m && !t.includes('PASS');
  if (m) {
    const all = Number(m[2]) === Number(m[3]);
    pass = pass && (m[1] === '✅ TRADE') === all;
  }
  return result('A8', pass, '"✅ TRADE" only at N/N, else "⏸️ No Trade"', t);
}

function checkA9(dom) {
  const narrow = dom.narrow || [];
  const over = narrow.filter(c => c.scrollWidth > c.clientWidth + 1).map(c => `${c.id} ${c.scrollWidth}>${c.clientWidth}`);
  const note = dom.pageOverflow ? ' (page-level overflow present: Known Issue, not failed)' : '';
  return result('A9', narrow.length > 0 && over.length === 0, 'no card wider than its box at 390px',
    narrow.length === 0 ? 'nothing measured' : over.length ? over.join(', ') : `${narrow.length} cards fit${note}`);
}

function runChecks(dom, api, helpers) {
  const d = dom || {};
  const a = api || {};
  if (d.error) return CHECK_IDS.map(id => result(id, false, 'analysis loads', `error banner: ${norm(d.error).slice(0, 120)}`));
  const fns = { A1: checkA1, A2: checkA2, A3: checkA3, A4: checkA4, A5: checkA5, A6: checkA6, A8: checkA8, A9: checkA9 };
  return CHECK_IDS.map(id => {
    try { return fns[id](d, a, helpers || {}); }
    catch (err) { return result(id, false, 'check runs', `check threw: ${err.message}`); }
  });
}

module.exports = { runChecks, CHECK_IDS, NAMES };
