#!/usr/bin/env node
/**
 * Data Sources tab statement audit, step 1 (Day 136): dump what the TAB showed and what it received, for
 * backend/audit_data_sources_tab.py to check. Plan: docs/claude/design/DATA_SOURCES_PROVENANCE_PLAN_DAY136.md (Part C).
 * Usage: node scripts/dump_data_sources_tab.js OUT_DIR TICKER [TICKER...]
 * Writes OUT_DIR/dump_<TICKER>.json = { ticker, runAt, payloads {stock, provenance, health, cache, coverage}, tab {...text by testid} }.
 * Reads the payloads the page itself fetched (network capture), never a second fetch. Use headless: 'shell' if it hangs.
 */
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');
const { readTabInPage } = require('./lib/readDataSourcesTab');

const FRONTEND = process.env.STA_FRONTEND || 'http://localhost:3000';
const KEYS = (t) => ({
  [`/api/stock/${t}`]: 'stock', [`/api/provenance/${t}`]: 'provenance', '/api/health': 'health',
  '/api/cache/status': 'cache', '/api/data-sources/coverage': 'coverage',
});

async function dump(browser, ticker, outDir) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 1000 });
  const payloads = {};
  const keys = KEYS(ticker);
  page.on('response', async (res) => {
    try {
      const p = new URL(res.url()).pathname;
      if (keys[p]) payloads[keys[p]] = { status: res.status(), body: await res.json() };   // the last response wins
    } catch (_) { /* not json / aborted: left out, the audit reports it as missing */ }
  });
  await page.goto(FRONTEND, { waitUntil: 'networkidle2', timeout: 60000 });
  const input = await page.waitForSelector('input[placeholder*="ticker"]', { timeout: 8000 });
  await input.click({ clickCount: 3 });
  await input.type(ticker, { delay: 25 });
  await page.keyboard.press('Enter');
  await page.waitForSelector('[data-testid="card-technical-read"], [data-testid="analysis-error"]', { timeout: 120000 });
  await new Promise((r) => setTimeout(r, 2000));
  const opened = await page.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((x) => x.textContent.includes('Data Sources'));
    if (b) { b.click(); return true; }
    return false;
  });
  if (!opened) throw new Error('Data Sources tab button not found');
  await page.waitForSelector('[data-testid="data-sources-tab"]', { timeout: 8000 });
  await page.waitForNetworkIdle({ idleTime: 1000, timeout: 30000 }).catch(() => {});
  await new Promise((r) => setTimeout(r, 800));

  const tab = await page.evaluate(readTabInPage);
  fs.writeFileSync(path.join(outDir, `dump_${ticker}.json`), JSON.stringify({ ticker, runAt: new Date().toISOString(), payloads, tab }, null, 1));
  await page.close();
}

(async () => {
  const [outDir, ...tickers] = process.argv.slice(2);
  if (!outDir || !tickers.length) { console.error('usage: dump_data_sources_tab.js OUT_DIR TICKER...'); process.exit(2); }
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await puppeteer.launch({ headless: process.env.STA_HEADLESS || 'shell' });
  let bad = 0;
  for (const t of tickers) {
    try { await dump(browser, t.toUpperCase(), outDir); console.log('dumped', t); } catch (e) { bad++; console.error('FAILED', t, e.message); }
  }
  await browser.close();
  process.exit(bad ? 1 : 0);
})();
