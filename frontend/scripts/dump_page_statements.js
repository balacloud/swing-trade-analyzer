#!/usr/bin/env node
/**
 * Statement Audit, step 1 (Day 126): dump what the PAGE showed and received, for backend/audit_statements.py to check.
 * Usage: node scripts/dump_page_statements.js OUT_DIR TICKER [TICKER...]
 * Writes OUT_DIR/dump_<TICKER>.json = { ticker, runAt (ISO, UTC), etNow, payloads {stock, sr, patterns, quote, spy},
 *   tr: {text (whole Technical Read card, closed <details> opened, spaces between elements, title/aria-label included), tokens[]},
 *   header: {testid -> text}, gauge: {...data attributes} }.
 * It reads the payloads the page itself fetched (network capture), never a second fetch.
 */
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

const FRONTEND = 'http://localhost:3000';
const KEYS = (t) => ({
  [`/api/stock/${t}`]: 'stock', [`/api/sr/${t}`]: 'sr', [`/api/patterns/${t}`]: 'patterns',
  [`/api/quote/${t}`]: 'quote', '/api/market/spy': 'spy',
  [`/api/breakout/${t}`]: 'breakout', [`/api/earnings/${t}`]: 'earnings', '/api/sectors/rotation': 'sectors',
  [`/api/fundamentals/${t}`]: 'fundamentals', [`/api/mr/signal/${t}`]: 'mr', '/api/market/index/QQQ': 'qqq', '/api/market/vix': 'vix', '/api/fear-greed': 'feargreed',
});

async function dump(browser, ticker, outDir) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 1000 });
  const payloads = {};
  const keys = KEYS(ticker);
  page.on('response', async (res) => {
    try {
      const p = new URL(res.url()).pathname;
      if (keys[p]) {
        const entry = { status: res.status(), body: await res.json(), url: res.url() };
        payloads[keys[p]] = entry;                                   // the last response wins (as before)
        (payloads[`${keys[p]}_all`] = payloads[`${keys[p]}_all`] || []).push(entry);   // every response kept (sector rotation is fetched twice)
      }
    } catch (_) { /* not json / aborted: left out, the audit reports it as missing */ }
  });
  await page.goto(FRONTEND, { waitUntil: 'networkidle2', timeout: 60000 });
  const input = await page.waitForSelector('input[placeholder*="ticker"]', { timeout: 8000 });
  await input.click({ clickCount: 3 });
  await input.type(ticker, { delay: 25 });
  await page.keyboard.press('Enter');
  await page.waitForSelector('[data-testid="card-technical-read"], [data-testid="analysis-error"]', { timeout: 120000 });
  await new Promise((r) => setTimeout(r, 2500));      // let the live quote and late panels settle
  // Price & Relative Strength is collapsed by default: open it so the two cards render. The breakout card loads later than the rest.
  await page.evaluate(() => { if (!document.querySelector('[data-testid="card-price-data"]')) { const b = document.querySelector('[data-testid="toggle-price-rs"]'); if (b) b.click(); } });
  await page.waitForSelector('[data-testid="card-breakout"]', { timeout: 20000 }).catch(() => {});
  await new Promise((r) => setTimeout(r, 1500));

  const out = await page.evaluate(() => {
    // text of an element with a space between every element, closed <details> opened, title/aria-label added
    const walk = (root) => {
      root.querySelectorAll('details').forEach((d) => { d.open = true; });
      const parts = [];
      const rec = (n) => {
        if (n.nodeType === 3) { parts.push(n.textContent); return; }
        if (n.nodeType !== 1) return;
        const t = n.getAttribute && (n.getAttribute('title') || n.getAttribute('aria-label'));
        if (t) parts.push(` [${t}] `);
        parts.push(' ');
        n.childNodes.forEach(rec);
        parts.push(' ');
      };
      rec(root);
      return parts.join('').replace(/\s+/g, ' ').trim();
    };
    const q = (id) => document.querySelector(`[data-testid="${id}"]`);
    const tr = q('card-technical-read');
    const hdrIds = ['live-price', 'live-change', 'live-status', 'price-as-of'];
    const header = {};
    hdrIds.forEach((id) => { const e = q(id); header[id] = e ? e.textContent.replace(/\s+/g, ' ').trim() : null; });
    const rows = (sel) => [...document.querySelectorAll(sel)].map((e) => ({ key: e.dataset.key, price: e.dataset.price, gap: e.dataset.gap, off: e.dataset.off || '' }));
    const cardTexts = {};
    ['card-trade-setup', 'card-breakout', 'card-price-data', 'card-relative-strength', 'card-stock-header', 'card-fundamentals', 'card-market-backdrop', 'card-mr-read'].forEach((id) => { const e = q(id); cardTexts[id] = e ? walk(e) : null; });
    const toggle = q('toggle-price-rs');
    return {
      cardTexts, priceRsToggle: toggle ? walk(toggle) : null,
      sizePlanPresent: !!q('size-this-plan'),
      etNow: new Date().toLocaleString('en-US', { timeZone: 'America/New_York' }),
      tr: tr ? { text: walk(tr) } : null,
      header,
      gauge: {
        ticks: rows('[data-testid="timing-tick"]'),
        ladder: rows('[data-testid="timing-ladder-row"]'),
        now: (() => { const n = q('timing-now-row'); return n ? { price: n.dataset.price, name: (q('timing-now-name') || {}).textContent } : null; })(),
        sentence: (q('timing-sentence') || {}).textContent || null,
        sub: (q('timing-sub') || {}).textContent || null,
        basis: (q('timing-basis') || {}).textContent || null,
        dotNote: (q('timing-dot-note') || {}).textContent || null,
        closeNote: (q('timing-close-note') || {}).textContent || null,
      },
    };
  });
  fs.writeFileSync(path.join(outDir, `dump_${ticker}.json`), JSON.stringify({ ticker, runAt: new Date().toISOString(), payloads, ...out }, null, 1));
  await page.close();
  return { ticker, got: Object.keys(payloads).join(','), trChars: out.tr ? out.tr.text.length : 0 };
}

(async () => {
  const [outDir, ...tickers] = process.argv.slice(2);
  if (!outDir || tickers.length === 0) { console.error('usage: node scripts/dump_page_statements.js OUT_DIR TICKER...'); process.exit(2); }
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await puppeteer.launch({ headless: 'shell', args: ['--no-sandbox'] });
  for (const t of tickers) {
    try { console.log(JSON.stringify(await dump(browser, t, outDir))); }
    catch (e) { console.error(`dump failed for ${t}: ${e.message}`); }
  }
  await browser.close();
})();
