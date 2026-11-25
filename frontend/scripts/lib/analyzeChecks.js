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

// Day 126: A8 (Simple view badge) removed with the Simple Checklist; its absence is now part of A2.
// Day 126: A10 added with the simple S&R switch (7 -> 8 checks).
// Day 126: A11 added with the Data Sources tab v2 (8 -> 9 checks).
// Day 126: A12 added with the entry-timing ruler (9 -> 10 checks); A13 with the live price line (10 -> 11).
// Day 127: A14 added (11 -> 12 checks) after /api/sr answered with NaN (invalid JSON) for 15 tickers and the runner only warned.
// Day 133: A15 added (12 -> 13 checks) with the Trade Setup live-price note (plan behind the live price); plan PLAN_VOID_BELOW_SUPPORT_PLAN_DAY133.md.
const CHECK_IDS = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15'];
const NAMES = {
  A1: 'Card order (backdrop first)',
  A2: 'Removed elements absent',
  A3: 'Market backdrop matches API',
  A4: 'Classification line',
  A5: 'Earnings badge and wording',
  A6: 'No blank cards',
  A9: 'Cards fit at 390px',
  A10: 'Buy and level rows match /api/sr',
  A11: 'Data Sources tab matches the backend',
  A12: 'Entry gauge and ladder match the data',
  A13: 'Live price line matches /api/quote',
  A14: 'Price answers are valid JSON with a real price',
  A15: 'Trade Setup says when the live price is below its support zone',
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
const money2 = (v) => `$${v.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;

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
  // Day 126: the Simple Checklist (toggle, TRADE/No Trade badge, "N/9 criteria met") is gone.
  if (full.includes('Simple Checklist')) found.push('"Simple Checklist"');
  if (/\bcriteria met\b/.test(full)) found.push('"criteria met"');
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

function checkA9(dom) {
  const narrow = dom.narrow || [];
  const over = narrow.filter(c => c.scrollWidth > c.clientWidth + 1).map(c => `${c.id} ${c.scrollWidth}>${c.clientWidth}`);
  const note = dom.pageOverflow ? ' (page-level overflow present: Known Issue, not failed)' : '';
  return result('A9', narrow.length > 0 && over.length === 0, 'no card wider than its box at 390px',
    narrow.length === 0 ? 'nothing measured' : over.length ? over.join(', ') : `${narrow.length} cards fit${note}`);
}

// A10 (Day 126): the Trade Setup's Buy and its Support/Resistance rows must say what /api/sr says
// (SIMPLE_SR_SWITCH_PLAN_DAY126.md §5). Expected text is built from the payload with the card's own
// formatter (formatZoneRange, passed in), so a change to either side that makes them disagree fails.
function checkA10(dom, api, h) {
  const sr = api.sr;
  if (!sr || sr.status == null) return result('A10', false, '/api/sr payload', '/api/sr response not captured');
  const fmt = h && h.formatZoneRange;
  if (typeof fmt !== 'function') return result('A10', false, 'formatZoneRange helper', 'helper not provided');
  const rows = dom.levelRows || {};
  if (sr.status !== 200 || !sr.body) {
    const shown = dom.planBuy || rows.support || rows.resistance;
    return result('A10', !shown, 'no Buy price and no level rows when /api/sr failed',
      shown ? 'page shows a Buy or level rows although /api/sr failed' : `none shown (status ${sr.status})`);
  }
  const b = sr.body;
  const zones = b.meta && b.meta.zones;
  if (!Array.isArray(zones)) return result('A10', false, '/api/sr meta.zones', 'payload has no meta.zones (old engine format?)');
  const problems = [];
  const sup = Array.isArray(b.support) ? b.support.filter(Number.isFinite) : [];
  // Day 127: the Buy is the last COMPLETED close when that close is inside the nearest support zone, else the zone high (= max(support)).
  // Worked out here from the zones and the close, NOT copied from suggestedEntry, so the payload is still checked.
  const nearestSup = zones.find(q => q && q.nearest === true && q.side === 'support');
  const lastClose = b.meta && b.meta.candle && b.meta.candle.barComplete === false && b.meta.prevBar && Number.isFinite(b.meta.prevBar.close) ? b.meta.prevBar.close : b.currentPrice;
  const closeInside = !!nearestSup && Number.isFinite(lastClose) && nearestSup.low <= lastClose && lastClose <= nearestSup.high;
  const entry = closeInside ? Math.round(lastClose * 100) / 100 : (sup.length ? Math.max(...sup) : null);
  if ((entry === null ? null : entry) !== (b.suggestedEntry == null ? null : b.suggestedEntry)) problems.push(`suggestedEntry ${b.suggestedEntry} != ${closeInside ? 'the last close (inside the nearest support zone)' : 'max(support)'} ${entry}`);
  if (entry !== null) {
    const want = `$${entry.toFixed(2)}`;
    const ts = (dom.cards || []).find(c => c.id === 'card-trade-setup');
    if (dom.planBuy != null) { if (norm(dom.planBuy) !== want) problems.push(`Buy tile ${norm(dom.planBuy)} != ${want}`); }
    else if (!ts || !norm(ts.text).includes(want)) problems.push(`Trade Setup does not show Buy ${want}`);
  } else if (dom.planBuy != null) problems.push('Buy shown but /api/sr has no support');
  for (const side of ['support', 'resistance']) {
    const z = zones.find(q => q && q.nearest === true && q.side === side);
    const text = norm(rows[side]);
    if (!text) { problems.push(`${side} row not found`); continue; }
    if (z) {
      const want = fmt(z.low, z.high);
      if (!text.includes(want)) problems.push(`${side} row "${text}" lacks ${want}`);
      const edge = side === 'support' ? z.high : z.low;
      const api_edge = side === 'support' ? b.suggestedEntry : b.suggestedTarget;
      if (api_edge !== edge && !(side === 'support' && closeInside)) problems.push(`${side} zone edge ${edge} != ${side === 'support' ? 'suggestedEntry' : 'suggestedTarget'} ${api_edge}`);
    } else if (!text.includes('None within')) problems.push(`${side} row should say "None within…" (no zone): "${text}"`);
  }
  return result('A10', problems.length === 0, 'Buy and Support/Resistance rows equal the /api/sr nearest zones', problems.join('; ') || 'ok');
}

// A11 (Day 126): the Data Sources tab must say what the backend says, and must never hide a failing data-quality verdict.
// Expected values come from /api/stock (identity), /api/provenance (source, quality) and /api/health (chains). Known
// tickers also carry a hard expectation, so a backend regression cannot hide behind a tab that faithfully repeats it:
// SOXL.NE's cached history is close-only with an unadjusted split and must show FAIL (the bug this tab was rebuilt for).
const KNOWN_VERDICT = { 'SOXL.NE': 'FAIL' };
// Day 126: tickers in backend/reference/known_splits.json that providers leave unadjusted: the tab must show STA's split line for them.
const KNOWN_SPLIT_TEXT = { 'SOXL.NE': '3-for-1 on 2026-05-25' };

function checkA11(dom, api, h) {
  const ds = dom.ds;
  if (!ds || ds.present !== true) return result('A11', false, 'Data Sources tab renders', (ds && ds.note) || 'tab did not render');
  const provOk = ok(api.provenance);
  const problems = [];
  if (!provOk) {
    if (!ds.error) problems.push(`/api/provenance failed (status ${api.provenance && api.provenance.status}) but the tab shows no error and Retry`);
    return result('A11', problems.length === 0, 'an error with Retry when /api/provenance fails', problems.join('; ') || 'error shown');
  }
  const qState = api.provenance.body.quality && api.provenance.body.quality.state;
  if (ds.error && qState !== 'error') problems.push('tab shows an error although /api/provenance answered');
  const s = ok(api.stock) ? api.stock.body : null;
  const label = (h && h.providerLabel) || ((x) => x);
  if (s) {
    const want = { exchange: s.exchange || 'unknown', currency: s.currency || 'unknown', cls: s.instrumentClass || 'Unknown' };
    for (const k of ['exchange', 'currency', 'cls']) if (norm(ds[k]) !== want[k]) problems.push(`${k} "${norm(ds[k])}" != "${want[k]}" (/api/stock)`);
  } else problems.push('/api/stock not captured, identity cannot be checked');
  const src = api.provenance.body.ohlcv && api.provenance.body.ohlcv.source;
  const wantFrom = src && src !== 'unknown' ? label(src) : 'unknown';
  if (norm(ds.dataFrom) !== wantFrom) problems.push(`data from "${norm(ds.dataFrom)}" != "${wantFrom}" (provenance source)`);
  const q = api.provenance.body.quality;
  if (q && q.state === 'ok') {
    const bad = Object.values(q.checks || {}).filter(c => c.level === 'WARN' || c.level === 'FAIL');
    if (ds.verdict !== q.level) problems.push(`verdict ${ds.verdict} != backend level ${q.level}`);
    if ((ds.qualityRows || []).length !== bad.length) problems.push(`${(ds.qualityRows || []).length} quality rows shown, backend has ${bad.length} WARN/FAIL checks`);
    if (q.level === 'FAIL' && !(ds.qualityRows || []).some(r => r.level === 'FAIL')) problems.push('backend level FAIL but no FAIL row is shown');
    if (!bad.length && !ds.allPass) problems.push('all checks pass but the tab does not say so');
  } else if (q && q.state === 'error') {
    if (!ds.error) problems.push('quality state error but the tab shows no error');
  } else if (q && q.state === 'not_cached') {
    if (ds.verdict) problems.push('nothing cached but a verdict is shown');
  } else problems.push('no quality block in /api/provenance');
  if (KNOWN_VERDICT[dom.ticker] && ds.verdict !== KNOWN_VERDICT[dom.ticker]) problems.push(`${dom.ticker} must show ${KNOWN_VERDICT[dom.ticker]}, tab shows ${ds.verdict}`);
  const adjusted = ((q && q.facts && q.facts.splits) || []).filter(x => x.status === 'unadjusted');
  if ((ds.splitNotes || []).length !== adjusted.length) problems.push(`${(ds.splitNotes || []).length} split notes shown, backend adjusted ${adjusted.length} split(s)`);
  if (KNOWN_SPLIT_TEXT[dom.ticker] && !(ds.splitNotes || []).some(n => n.includes(KNOWN_SPLIT_TEXT[dom.ticker]))) problems.push(`${dom.ticker} must show the split-adjusted line "${KNOWN_SPLIT_TEXT[dom.ticker]}"`);
  const chains = ok(api.health) && api.health.body.providers && api.health.body.providers.chains;
  if (chains && Array.isArray(chains.ohlcv)) {
    const got = (ds.chainRows || []).filter(r => r.group === 'price').map(r => r.provider);
    if (got.join() !== chains.ohlcv.join()) problems.push(`price chain "${got.join('>')}" != backend "${chains.ohlcv.join('>')}"`);
  } else problems.push('/api/health chains not captured');
  // Day 126: the "how indicators are calculated" table must be the catalog the backend sent: same names, a "From" and a "How" on every row.
  const want = api.provenance.body.indicators;
  if (Array.isArray(want)) {
    const rows = ds.indicatorRows || [];
    if (rows.length !== want.length) problems.push(`indicator table has ${rows.length} rows, backend sent ${want.length}`);
    else want.forEach((w, i) => { if (norm(rows[i][0]) !== w.name) problems.push(`indicator row ${i + 1} "${norm(rows[i][0])}" != "${w.name}"`); });
    if (rows.some(r => !r[1] || !r[2])) problems.push('an indicator row has an empty From or How');
  } else if (!ds.indicatorsUnavailable) problems.push('backend sent no indicators and the tab does not say so');
  if ((ds.chainRows || []).some(r => r.provider === 'stooq')) problems.push('Stooq (disabled) is listed in a chain');
  return result('A11', problems.length === 0, 'tab identity, source, quality verdict and chain equal the backend', problems.join('; ') || `verdict ${ds.verdict || 'none'}, identity and chain match`);
}

// A12 (Day 126): the "Price vs its 21-day average" gauge shows REAL numbers: the dot carries the page price, the tick marks are the 21, 50 and
// 200-day averages, and the old verdict wording is gone.
function checkA12(dom, api) {
  const t = dom.timing;
  if (!t) return result('A12', false, 'entry gauge reader', 'page reader did not return timing');
  const atr = api.sr && api.sr.body && api.sr.body.meta && api.sr.body.meta.atr;
  const goodAtr = Number.isFinite(atr) && atr > 0;
  const tr = (dom.cards || []).find(c => c.id === 'card-technical-read');
  const problems = [];
  if (tr && /Not yet, |Yes, close to|Yes, a little extended|Is now a good moment/.test(tr.text)) problems.push('old verdict wording is still on the card');
  // Day 126: the Strong/Developing/Weak headline and its sentence were turned into a plain facts block
  if (tr && /Strong needs all three|How this read was formed|market leader right now|healthy uptrend and beating the market|boxes are checked/.test(tr.text)) problems.push('the old verdict headline or its wording is still on the Technical Read card');
  // Day 126: the volume one-word answer (Yes / Mixed / No, sellers lead) became a plain count of the three signals
  if (tr && /No, sellers lead|No clear lean|No, heavy selling|signals disagree|Are buyers behind the move/.test(tr.text)) problems.push('the old volume verdict wording is still on the Technical Read card');
  if (tr && !/Trend, momentum and strength against the market/.test(tr.text)) problems.push('the facts block title is missing from the Technical Read card');
  if (!t.present) {
    if (!t.unavailable) problems.push('neither the gauge nor a "Can\'t tell" reason is shown');
    else if (goodAtr && !/200 days/.test(t.unavailable)) problems.push(`"${norm(t.unavailable)}" shown although /api/sr has an ATR`);
    return result('A12', problems.length === 0, 'gauge, or an honest reason it cannot be drawn', problems.join('; ') || `not drawn: ${norm(t.unavailable)}`);
  }
  if (!ok(api.stock)) return result('A12', false, 'stock payload', 'stock response not captured');
  // Day 126: with a usable live quote the gauge measures from it; otherwise from the /api/stock price
  const qb = ok(api.quote) ? api.quote.body : null;
  const liveUsable = !!qb && qb.available === true && qb.session !== 'closed' && Number.isFinite(qb.price) && qb.price > 0;
  const price = liveUsable ? qb.price : api.stock.body.currentPrice;
  if (Number.isFinite(price) && norm(t.price) !== money2(price)) problems.push(`dot price ${norm(t.price)} != ${liveUsable ? 'live' : 'page'} price ${money2(price)}`);
  if (t.sentence && !norm(t.sentence).startsWith(norm(t.price))) problems.push(`sentence "${norm(t.sentence).slice(0, 40)}" does not start with the dot price ${norm(t.price)}`);
  if (!liveUsable && t.basis && !/\(last close\)/.test(norm(t.basis))) problems.push(`no live price but the basis label says "${norm(t.basis)}"`);
  if (liveUsable && t.basis && /\(last close\)/.test(norm(t.basis))) problems.push('live price but the basis label says last close');
  const k = t.ticks || [];
  if (k.length < 1 || k.length > 3 || k.some(x => !Number.isFinite(x) || !(x > 0))) problems.push(`expected 1 to 3 gauge marks that are positive prices, found ${k.length}`);
  else if (k.some((x, i) => i > 0 && x < k[i - 1])) problems.push('gauge marks are not in price order');
  if (!goodAtr) problems.push('gauge drawn although /api/sr has no ATR');
  // Day 126 ladder: the page checked against itself (the averages are computed in the browser, so there is no outside copy to compare with)
  const lad = t.ladder || [];
  const keys = t.tickKeys || [];
  if (lad.length !== k.length) problems.push(`ladder has ${lad.length} average rows but the gauge has ${k.length} marks`);
  else keys.forEach((key, i) => {
    const row = lad.find(r => r.key === key);
    if (!row) problems.push(`gauge mark "${key}" has no ladder row`);
    else if (Math.abs(row.price - k[i]) > 0.005) problems.push(`ladder ${key} ${row.price} != gauge mark ${k[i]}`);
    else {
      const wantGap = (pageP => (pageP - row.price) / row.price * 100)(Number(String(norm(t.price)).replace(/[^0-9.\-]/g, '')));
      if (!Number.isFinite(row.gap) || Math.abs(row.gap - wantGap) > 0.1) problems.push(`ladder ${key} gap ${row.gap} != price vs average ${wantGap.toFixed(1)}`);
    }
  });
  if (!t.nowRow) problems.push('ladder has no price row');
  else {
    if (norm(t.price) !== money2(t.nowRow.price)) problems.push(`ladder price row ${t.nowRow.price} != dot price ${norm(t.price)}`);
    const basisWords = norm(t.basis).replace(/^\(|\)$/g, '').toLowerCase();
    if (basisWords && norm(t.nowRow.name).toLowerCase() !== basisWords) problems.push(`ladder price row says "${norm(t.nowRow.name)}" but the basis label says "${basisWords}"`);
  }
  const order = t.ladderOrder || [];
  if (order.length < 2 || order.some((x, i) => !Number.isFinite(x) || (i > 0 && x > order[i - 1]))) problems.push('ladder is not in price order, highest first');
  return result('A12', problems.length === 0, 'dot = page price, ladder = gauge marks, gaps = price vs average, no verdict wording', problems.join('; ') || `dot ${norm(t.price)}, marks ${k.map(x => x.toFixed(2)).join(' / ')}`);
}

// A13 (Day 126): the live price line shows what /api/quote sent, with its trade time; the "Last close" line is the quote's own;
// the gauge "Last close" note exists only with a usable live price (no amber marker any more); every other state is said out loud, never a stale close posing as live.
function checkA13(dom, api) {
  const L = dom.live;
  if (!L) return result('A13', false, 'live price reader', 'page reader did not return live');
  const q = api.quote;
  const problems = [];
  const body = ok(q) ? q.body : null;
  if (!body) {
    problems.push('/api/quote response not captured');
    return result('A13', false, 'live price line equals /api/quote', problems.join('; '));
  }
  const usable = body.available === true && body.session !== 'closed' && Number.isFinite(body.price) && body.price > 0;
  // Day 126: the amber live-tick marker is gone (the gauge bubble IS the live price); a "Last close" note shows with a usable live price
  if (L.tickCount !== 0) problems.push(`${L.tickCount} live-tick marker(s), expected none`);
  const noteWanted = usable && dom.timing && dom.timing.present && body.last_close && Number.isFinite(body.last_close.price);
  if (noteWanted && !norm(L.timingNote).startsWith(`Last close ${money2(body.last_close.price)}`)) problems.push(`gauge close note "${norm(L.timingNote)}" != quote last close ${money2(body.last_close.price)}`);
  if (!noteWanted && L.timingNote) problems.push(`gauge close note "${norm(L.timingNote)}" shown without a usable live price`);
  if (usable) {
    if (norm(L.priceText) !== `Now ${money2(body.price)}`) problems.push(`live price "${norm(L.priceText)}" != "Now ${money2(body.price)}"`);
    if (!/last trade \d{1,2}:\d{2}(am|pm) ET/.test(norm(L.statusText))) problems.push(`no trade time in "${norm(L.statusText)}"`);
    const lc = body.last_close;
    if (lc && Number.isFinite(lc.price)) {
      if (!norm(L.closeText).startsWith(`Last close ${money2(lc.price)}`)) problems.push(`close line "${norm(L.closeText)}" != quote last close ${money2(lc.price)}`);
      const up = body.price - lc.price >= 0;
      if (L.changeText && up !== !/^\(\u2212/.test(norm(L.changeText))) problems.push(`change "${norm(L.changeText)}" has the wrong sign`);
    }
  } else {
    if (L.priceText) problems.push(`"${norm(L.priceText)}" shown although the quote has no usable live price`);
    const want = body.available === true ? /closed/ : /unavailable/;
    if (!want.test(norm(L.statusText))) problems.push(`state not said out loud (wanted ${want}, got "${norm(L.statusText)}")`);
  }
  return result('A13', problems.length === 0, 'live line, close line and gauge marker equal /api/quote; other states shown in words',
    problems.join('; ') || (usable ? `${money2(body.price)} · ${norm(L.statusText)}` : `${body.available === true ? 'market closed' : 'unavailable (' + body.reason + ')'} shown in words`));
}

// A14 (Day 127): the two price answers the page is built on must be valid JSON with a real current price. A cached bar with no
// close price once made /api/sr answer `"currentPrice": NaN` (invalid JSON); the runner only printed a warning and every other
// check still passed. A failed (non-200) answer is left to the checks that already cover an error banner.
function checkA14(dom, api) {
  const problems = [];
  for (const key of ['stock', 'sr']) {
    const r = api && api[key];
    if (!r || r.status == null) { problems.push(`/api/${key} was not captured`); continue; }
    if (r.status !== 200) continue;
    if (r.body == null) { problems.push(`/api/${key} answered 200 but its body is not valid JSON (NaN?)`); continue; }
    const p = r.body.currentPrice;
    if (!(typeof p === 'number' && Number.isFinite(p) && p > 0)) problems.push(`/api/${key} currentPrice is not a real price (${p})`);
  }
  return result('A14', problems.length === 0, 'stock and S&R answers are valid JSON with a real current price', problems.join('; ') || 'ok');
}

// A15 (Day 133): when a usable regular-session live price is below the nearest support zone's low (or, with no zone, below the plan stop) the Trade Setup card
// says so in numbers: a banner with the live price, the zone, the card's own last close; the plan is marked, Size is replaced by a muted line, one live tick, and the
// Key Levels note says what price the levels were measured at. A pre-market / after-hours price only adds a muted fact line. Any other state: none of it appears.
// The expectation is derived here from /api/quote and /api/sr (not from planStatus.js), so a bug in either place shows as a mismatch.
function checkA15(dom, api, helpers) {
  const P = dom.planLive;
  if (!P) return result('A15', false, 'plan live-price reader', 'page reader did not return planLive');
  if (!ok(api.quote)) return result('A15', false, 'quote captured', '/api/quote response not captured');
  const qb = api.quote.body;
  const price = qb.price;
  const usable = qb.available === true && qb.session !== 'closed' && Number.isFinite(price) && price > 0;
  const body = ok(api.sr) ? api.sr.body : null;
  const supports = body && Array.isArray(body.support) ? body.support.filter(Number.isFinite) : [];
  const meta = (body && body.meta) || {};
  let want = null, zone = null, stop = null, entry = null;
  // the card shows no plan (so no note) when /api/sr has no support or no usable last close (PullbackPlan.jsx no_support / no_price)
  const lastCloseNow = body ? (meta.candle && meta.candle.barComplete === false && meta.prevBar && Number.isFinite(meta.prevBar.close) ? meta.prevBar.close : body.currentPrice) : null;
  if (usable && body && supports.length && Number.isFinite(lastCloseNow)) {
    zone = (Array.isArray(meta.zones) ? meta.zones : []).find(z => z && z.nearest === true && z.side === 'support' && Number.isFinite(z.low) && Number.isFinite(z.high)) || null;
    entry = Number.isFinite(body.suggestedEntry) ? body.suggestedEntry : Math.max(...supports);
    stop = Number.isFinite(meta.atr) && meta.atr > 0 ? Math.max(0.01, entry - 2 * meta.atr) : null;
    const below = zone ? price < zone.low : (stop != null && price < stop);
    if (below) want = qb.session === 'regular' ? 'void' : 'fact';
  }
  const problems = [];
  const has = (v) => v != null && norm(v) !== '';
  if (want == null) {
    if (has(P.voidText)) problems.push(`void note shown without a reason: "${norm(P.voidText).slice(0, 60)}"`);
    if (has(P.factText)) problems.push(`live-price fact line shown without a reason: "${norm(P.factText).slice(0, 60)}"`);
    if (P.tickCount !== 0) problems.push(`${P.tickCount} plan live tick(s), expected none`);
    if (has(P.sizeOff)) problems.push('"Sizing is off" shown although the live price is not below the plan');
    if (has(P.staleNote)) problems.push('Key Levels "Measured at" note shown without a reason');
    return result('A15', problems.length === 0, 'no live-price note unless a usable live price is below the support zone', problems.join('; ') || 'none shown, none expected');
  }
  const fz = (helpers && helpers.formatZoneRange) ? helpers.formatZoneRange(zone && zone.low, zone && zone.high) : null;
  const where = zone ? `below the support zone (${fz})` : `below this plan's stop (${money2(stop)})`;
  if (want === 'fact') {
    const t = norm(P.factText);
    if (!has(P.factText)) problems.push('pre/post-market price is below the zone but no fact line is shown');
    else {
      if (!t.startsWith(`${qb.session === 'pre' ? 'Pre-market price' : 'After-hours price'} ${money2(price)} (`)) problems.push(`fact line "${t.slice(0, 60)}" does not start with the ${qb.session} price ${money2(price)}`);
      if (!t.includes(where)) problems.push(`fact line does not say "${where}"`);
    }
    if (has(P.voidText)) problems.push('a pre/post-market price must not mark the plan void');
    if (P.tickCount !== 0) problems.push('a pre/post-market price must not draw the plan live tick');
    if (has(P.sizeOff)) problems.push('a pre/post-market price must not turn sizing off');
    return result('A15', problems.length === 0, 'pre/post-market: a muted fact line only', problems.join('; ') || `fact line: ${norm(P.factText).slice(0, 90)}`);
  }
  // want === 'void'
  const t = norm(P.voidText);
  if (!has(P.voidText)) return result('A15', false, `void note for live ${money2(price)} ${where}`, 'no void note on the card');
  if (!t.startsWith(`Last trade ${money2(price)} (`)) problems.push(`note "${t.slice(0, 60)}" does not start with the live price ${money2(price)}`);
  if (!t.includes(where)) problems.push(`note does not say "${where}"`);
  if (zone && stop != null && price < stop && !t.includes(`also below the stop (${money2(stop)})`)) problems.push(`price is below the stop ${money2(stop)} but the note does not say so`);
  if (zone && !(stop != null && price < stop) && /also below the stop/.test(t)) problems.push('note says "also below the stop" but the price is above the stop');
  const lastClose = meta.candle && meta.candle.barComplete === false && meta.prevBar && Number.isFinite(meta.prevBar.close) ? meta.prevBar.close : body.currentPrice;
  if (Number.isFinite(lastClose) && !t.includes(`set at the last close (${money2(lastClose)}`)) problems.push(`note does not quote the card's last close ${money2(lastClose)}`);
  if (Number.isFinite(entry) && (entry > price) !== /its Buy is above the price now/.test(t)) problems.push('"its Buy is above the price now" disagrees with Buy vs live price');
  // one quote (Golden Rule 63): the trade time in the note is the one in the page header
  const nt = t.match(/\((\d{1,2}:\d{2}(?:am|pm) ET)\)/);
  const ht = norm(dom.live && dom.live.statusText).match(/last trade (\d{1,2}:\d{2}(?:am|pm) ET)/);
  if (!nt) problems.push('no trade time in the note');
  else if (ht && nt[1] !== ht[1]) problems.push(`note trade time ${nt[1]} != header trade time ${ht[1]}`);
  if (has(P.factText)) problems.push('both the void note and the fact line are shown');
  // With no ATR the card shows the note and the buy/target text only (no stop, no bar, no sizing): no tick, no label, no sizing line
  const noAtr = !(Number.isFinite(meta.atr) && meta.atr > 0);
  if (noAtr) {
    if (P.tickCount !== 0) problems.push(`${P.tickCount} plan live tick(s), expected none (no ATR, no bar is drawn)`);
    if (P.sizeBtn) problems.push('"Size this plan" shown although there is no stop (no ATR)');
  } else {
    if (P.tickCount !== 1) problems.push(`${P.tickCount} plan live tick(s), expected 1`);
    if (!has(P.labelText)) problems.push('the plan live tick has no label');
    else if (/last trade/.test(norm(P.labelText)) && nt && !norm(P.labelText).includes(nt[1])) problems.push(`tick label "${norm(P.labelText)}" time differs from the note time`);
    if (P.sizeBtn) problems.push('"Size this plan" is still offered for a plan the live price is below');
    if (!has(P.sizeOff)) problems.push('the "Sizing is off" line is missing');
  }
  if (!has(P.staleNote) || !/^Measured at /.test(norm(P.staleNote))) problems.push('Key Levels "Measured at" note is missing');
  else if (Number.isFinite(body.currentPrice) && !norm(P.staleNote).includes(money2(body.currentPrice))) problems.push(`Key Levels note does not quote the /api/sr price ${money2(body.currentPrice)}`);
  if (/support has broken|no longer applies|plan is dead|broke/i.test(t)) problems.push('verdict wording in the note (facts only)');
  return result('A15', problems.length === 0, 'void note with the live price, zone, last close, trade time; plan marked; sizing off; one tick; Key Levels note', problems.join('; ') || `void: ${t.slice(0, 100)}`);
}

function runChecks(dom, api, helpers) {
  const d = dom || {};
  const a = api || {};
  if (d.error) return CHECK_IDS.map(id => result(id, false, 'analysis loads', `error banner: ${norm(d.error).slice(0, 120)}`));
  const fns = { A1: checkA1, A2: checkA2, A3: checkA3, A4: checkA4, A5: checkA5, A6: checkA6, A9: checkA9, A10: checkA10, A11: checkA11, A12: checkA12, A13: checkA13, A14: checkA14, A15: checkA15 };
  return CHECK_IDS.map(id => {
    try { return fns[id](d, a, helpers || {}); }
    catch (err) { return result(id, false, 'check runs', `check threw: ${err.message}`); }
  });
}

module.exports = { runChecks, CHECK_IDS, NAMES };
