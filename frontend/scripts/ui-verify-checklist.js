#!/usr/bin/env node
/**
 * Analyze page verifier (rewritten Day 124, Analyze Redesign Step 8).
 * Plan: docs/claude/design/ANALYZE_REDESIGN_STEP8_PLAN_DAY124.md (Fable-reviewed).
 *
 * Loads each ticker in the real app, records the JSON the page itself received
 * (market SPY/QQQ/VIX, stock, earnings), extracts the cards by data-testid, and
 * runs the pure checks in scripts/lib/analyzeChecks.js:
 *   A1 card order (backdrop first)      A5 earnings badge + wording
 *   A2 removed elements absent          A6 no blank cards
 *   A3 backdrop equals the API payload  (A8 Simple view badge: removed Day 126 with the checklist)
 *   A10 Buy and level rows equal /api/sr    A11 Data Sources tab equals /api/provenance, /api/stock, /api/health
 *   A12 Entry ruler: dot price = page price, tick spacing = the Trade Setup ATR, no verdict words
 *   A13 Live price line + ruler close note equal /api/quote; A12 ruler measures from the live price (Day 126)
 *   A4 classification (ETF, no Unknown) A9 cards fit at 390px
 * (A7 "data source shown" dropped: the app header shows it on every tab, so it
 * could never fail.) Unit tests for the checks: scripts/test_analyze_checks.mjs.
 *
 * Usage (backend :5001 and frontend :3000 running):
 *   cd frontend && node scripts/ui-verify-checklist.js            # default tickers
 *   node scripts/ui-verify-checklist.js AAPL SMH                  # specific tickers
 * Exit code: 0 only when every check on every ticker passes; 1 otherwise.
 * Report: docs/test/UI_Verify_<YYYYMMDD-HHMM>/REPORT.md (new folder per run).
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');
const http = require('http');
const { runChecks, CHECK_IDS, NAMES } = require('./lib/analyzeChecks');

const FRONTEND_URL = 'http://localhost:3000';
const BACKEND_URL = 'http://localhost:5001';
const ANALYSIS_TIMEOUT = 60000;
const SETTLE_TIMEOUT = 30000;
const PAGE_LOAD_TIMEOUT = 20000;
const BETWEEN_TICKERS_DELAY = 2000;
const NARROW_WIDTH = 390;

// AAPL / NVDA: large-cap equities; SMH: ETF (classification line); JPM: bank;
// RIVN: negative ROE, shorter history.
const DEFAULT_TICKERS = ['AAPL', 'NVDA', 'SMH', 'JPM', 'RIVN'];

function parseArgs() {
  const args = process.argv.slice(2);
  const removed = args.filter(a => a === '--holding' || a === '--all-periods');
  if (removed.length) {
    console.error(`${removed.join(', ')}: removed Day 123 with the Holding Period selector. Pass tickers only.`);
    process.exit(2);
  }
  const unknown = args.filter(a => a.startsWith('--'));
  if (unknown.length) {
    console.error(`Unknown option(s): ${unknown.join(', ')}`);
    process.exit(2);
  }
  const tickers = args.map(a => a.toUpperCase());
  return { tickers: tickers.length ? tickers : [...DEFAULT_TICKERS] };
}

async function checkServices() {
  for (const [name, url] of [['Backend', `${BACKEND_URL}/api/health`], ['Frontend', FRONTEND_URL]]) {
    try {
      await new Promise((resolve, reject) => {
        http.get(url, res => { res.resume(); res.statusCode === 200 ? resolve() : reject(new Error(`HTTP ${res.statusCode}`)); })
          .on('error', reject);
      });
      console.log(`  ${name}: OK`);
    } catch (err) {
      console.error(`  ${name}: NOT RUNNING (${err.message})`);
      return false;
    }
  }
  return true;
}

// Which captured payload a response URL belongs to (null = not one we check).
function captureKey(url, ticker) {
  let p;
  try { p = new URL(url).pathname; } catch { return null; }
  if (p === '/api/market/spy') return 'spy';
  if (p === '/api/market/index/QQQ') return 'qqq';
  if (p === '/api/market/vix') return 'vix';
  if (p === `/api/stock/${ticker}`) return 'stock';
  if (p === `/api/earnings/${ticker}`) return 'earnings'; // query string (?days=N) ignored
  if (p === `/api/quote/${ticker}`) return 'quote'; // Day 126: A13 compares the live price line to it
  if (p === `/api/sr/${ticker}`) return 'sr'; // Day 126: A10 compares the plan and level rows to this payload
  if (p === `/api/provenance/${ticker}`) return 'provenance'; // Day 126: A11 compares the Data Sources tab to it
  if (p === '/api/health') return 'health';                   // Day 126: A11 compares the source chain to providers.chains
  return null;
}

async function extractDom(page) {
  return page.evaluate(() => {
    const q = (sel) => document.querySelector(`[data-testid="${sel}"]`);
    const text = (el) => (el ? el.textContent : null);
    const err = q('analysis-error');
    const cards = [...document.querySelectorAll('[data-testid^="card-"]')]
      .map(el => {
        // Body = card text minus its title row/subtitle (marked data-card-head in the app).
        const marked = el.querySelector('[data-card-head]') !== null || el.dataset.testid === 'card-stock-header';
        let body;
        if (marked) {
          const clone = el.cloneNode(true);
          clone.querySelectorAll('[data-card-head]').forEach(h => h.remove());
          body = clone.textContent;
        }
        return { id: el.dataset.testid, text: el.textContent, bodyText: body, collapsed: el.dataset.collapsed === 'true' };
      });
    const shortTexts = [...document.body.querySelectorAll('*')]
      .filter(el => el.children.length === 0)
      .map(el => { const c = el.closest('[data-testid^="card-"]'); return { text: el.textContent.trim(), card: c ? c.dataset.testid : null }; })
      .filter(x => x.text && x.text.length <= 12);
    const backdropCard = q('card-market-backdrop');
    const rows = backdropCard ? [...backdropCard.querySelectorAll('[data-testid="backdrop-row"]')].map(r => ({
      label: r.dataset.label,
      long: text(r.querySelector('[data-testid="backdrop-long"]')),
      short: text(r.querySelector('[data-testid="backdrop-short"]')),
      drop: text(r.querySelector('[data-testid="backdrop-drop"]')),
      unavailable: text(r.querySelector('[data-testid="backdrop-unavailable"]')),
    })) : [];
    return {
      error: err ? err.textContent : null,
      cards,
      header: text(q('card-stock-header')),
      shortTexts,
      fullText: document.body.textContent,
      earningsBadge: !!q('earnings-badge'),
      timing: (() => {
        const r = q('timing-ruler');
        return {
          present: !!r,
          unavailable: text(q('timing-unavailable')),
          price: text(q('timing-price')),
          sentence: text(q('timing-sentence')),
          basis: text(q('timing-basis')),
          ticks: [...document.querySelectorAll('[data-testid="timing-tick"]')].map(t => parseFloat(t.dataset.price)),
          tickKeys: [...document.querySelectorAll('[data-testid="timing-tick"]')].map(t => t.dataset.key),
          ladder: [...document.querySelectorAll('[data-testid="timing-ladder-row"]')].map(t => ({ key: t.dataset.key, price: parseFloat(t.dataset.price), gap: t.dataset.gap === '' ? null : parseFloat(t.dataset.gap) })),
          nowRow: (() => { const n = q('timing-now-row'); return n ? { price: parseFloat(n.dataset.price), name: text(q('timing-now-name')), index: [...n.parentElement.children].indexOf(n) } : null; })(),
          ladderOrder: [...document.querySelectorAll('[data-testid="timing-ladder-row"], [data-testid="timing-now-row"]')].map(t => parseFloat(t.dataset.price)),
        };
      })(),
      live: {
        priceText: text(q('live-price')),
        changeText: text(q('live-change')),
        statusText: text(q('live-status')),
        closeText: text(q('price-as-of')),
        tickCount: document.querySelectorAll('[data-testid="live-tick"]').length,
        timingNote: text(q('timing-close-note')),
      },
      planLive: {   // Day 133 (A15): the Trade Setup live-price note, the plan's live tick, the sizing line and the Key Levels note
        voidText: text(q('plan-void')),
        factText: text(q('plan-live-fact')),
        tickCount: document.querySelectorAll('[data-testid="plan-live-tick"]').length,
        labelText: text(q('plan-live-label')),
        sizeOff: text(q('size-plan-off')),
        sizeBtn: !!q('size-this-plan'),
        staleNote: text(q('key-levels-stale-note')),
      },
      noteIntegrity: text(q('data-note-integrity')),   // Day 135 (A17): thin-data note under the header price
      noteTracking: text(q('data-note-tracking')),     // Day 135 (A17): leveraged fund's measured comparison
      freshText: text(q('price-freshness')),   // Day 135 (A16): the saved-prices line under the header price
      planBuy: text(q('plan-buy-value')),
      levelRows: { support: text(q('key-level-support')), resistance: text(q('key-level-resistance')) },
      backdrop: { rows, vix: text(backdropCard && backdropCard.querySelector('[data-testid="backdrop-vix"]')) },
    };
  });
}

// Day 126 (A11): open the Data Sources tab and read what it shows.
async function readDataSources(page) {
  const opened = await page.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find(x => x.textContent.includes('Data Sources'));
    if (b) { b.click(); return true; }
    return false;
  });
  if (!opened) return { present: false, note: 'Data Sources tab button not found' };
  try {
    await page.waitForSelector('[data-testid="data-sources-tab"]', { timeout: 8000 });
    await page.waitForNetworkIdle({ idleTime: 800, timeout: SETTLE_TIMEOUT });
  } catch { /* read whatever rendered */ }
  await new Promise(r => setTimeout(r, 500));
  return page.evaluate(() => {
    const q = (s) => document.querySelector(`[data-testid="${s}"]`);
    const t = (el) => (el ? el.textContent.trim() : null);
    const v = q('ds-quality-verdict');
    return {
      present: !!q('data-sources-tab'),
      error: !!q('ds-error'),
      symbol: t(q('ds-symbol')), exchange: t(q('ds-exchange')), currency: t(q('ds-currency')), cls: t(q('ds-class')), dataFrom: t(q('ds-datafrom')),
      verdict: v ? v.dataset.level : null,
      qualityRows: [...document.querySelectorAll('[data-testid="ds-quality-row"]')].map(r => ({ level: r.dataset.level, text: r.textContent.trim() })),
      allPass: !!q('ds-quality-allpass'),
      splitNotes: [...document.querySelectorAll('[data-testid="ds-split-note"]')].map(e => e.textContent.trim()),
      indicatorRows: [...document.querySelectorAll('[data-testid="ds-indicators"] tbody tr')].map(r => [...r.children].map(td => td.textContent.trim())),
      indicatorsUnavailable: !!q('ds-indicators-unavailable'),
      chainRows: [...document.querySelectorAll('[data-testid="ds-chain-row"]')].map(r => ({ group: r.dataset.group, provider: r.dataset.provider })),
    };
  });
}

async function measureNarrow(page) {
  await page.setViewport({ width: NARROW_WIDTH, height: 844 });
  await new Promise(r => setTimeout(r, 600));
  const m = await page.evaluate(() => ({
    narrow: [...document.querySelectorAll('[data-testid^="card-"]')]
      .map(el => ({ id: el.dataset.testid, scrollWidth: el.scrollWidth, clientWidth: el.clientWidth })),
    pageOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
  }));
  await page.setViewport({ width: 1440, height: 900 });
  await new Promise(r => setTimeout(r, 300));
  return m;
}

async function verifyTicker(page, ticker, index, total, helpers) {
  const label = `[${index}/${total}] ${ticker}`;
  console.log(`\n${label}: analyzing...`);
  const api = { spy: { status: null, body: null }, qqq: { status: null, body: null }, vix: { status: null, body: null },
    stock: { status: null, body: null }, earnings: { status: null, body: null }, sr: { status: null, body: null },
    provenance: { status: null, body: null }, health: { status: null, body: null }, quote: { status: null, body: null } };
  let recording = false;
  const pending = [];
  const onResponse = (res) => {
    if (!recording) return;
    const key = captureKey(res.url(), ticker);
    if (!key) return;
    pending.push(res.json()
      .then(body => { api[key] = { status: res.status(), body }; })
      .catch(err => { api[key] = { status: res.status(), body: null }; console.warn(`  ${key}: response body unreadable (${err.message})`); }));
  };
  page.on('response', onResponse);

  try {
    await page.goto(FRONTEND_URL, { waitUntil: 'networkidle2', timeout: PAGE_LOAD_TIMEOUT });
    await page.waitForSelector('input[placeholder*="ticker"]', { timeout: 5000 });
    recording = true; // only responses caused by this analysis
    const input = await page.$('input[placeholder*="ticker"]');
    await input.click({ clickCount: 3 });
    await input.type(ticker, { delay: 30 });
    await page.keyboard.press('Enter');

    await page.waitForSelector('[data-testid="card-technical-read"], [data-testid="analysis-error"]', { timeout: ANALYSIS_TIMEOUT });
    // Let the per-card fetches (MR, S&R, earnings...) finish before reading.
    try { await page.waitForNetworkIdle({ idleTime: 1000, timeout: SETTLE_TIMEOUT }); }
    catch { console.warn(`  ${ticker}: network still busy after ${SETTLE_TIMEOUT / 1000}s; reading anyway`); }
    try {
      await page.waitForFunction(() => !document.body.textContent.includes('Checking the dip rules'), { timeout: SETTLE_TIMEOUT });
    } catch { console.warn(`  ${ticker}: MR card still loading`); }
    await Promise.all(pending);

    const dom = await extractDom(page);
    dom.ticker = ticker;
    if (!dom.error) {
      Object.assign(dom, await measureNarrow(page));
      dom.ds = await readDataSources(page);   // after the narrow measure: it leaves the Analyze tab
      await Promise.all(pending);
    }
    recording = false;

    const checks = runChecks(dom, api, helpers);
    const failed = checks.filter(c => !c.pass);
    console.log(`${label}: ${checks.length - failed.length}/${checks.length} pass${dom.pageOverflow ? ' (page-level 390px overflow: Known Issue)' : ''}`);
    for (const c of failed) console.log(`  ❌ ${c.id} ${c.name}: expected ${c.expected} | got ${c.actual}`);
    return { ticker, checks, error: dom.error || null, pageOverflow: !!dom.pageOverflow };
  } catch (err) {
    console.error(`${label}: FAILED - ${err.message}`);
    return { ticker, checks: CHECK_IDS.map(id => ({ id, name: NAMES[id], pass: false, expected: 'run', actual: `runner error: ${err.message}` })), error: err.message };
  } finally {
    page.off('response', onResponse);
  }
}

function generateReport(results, outputDir) {
  const all = results.flatMap(r => r.checks);
  const passed = all.filter(c => c.pass).length;
  const lines = [
    '# Analyze Page Verification Report',
    '',
    `**Date:** ${new Date().toISOString()}`,
    `**Tickers:** ${results.map(r => r.ticker).join(', ')}`,
    `**Checks passed:** ${passed}/${all.length}`,
    '',
    '| Ticker | ' + CHECK_IDS.join(' | ') + ' | Note |',
    '|---|' + CHECK_IDS.map(() => '---').join('|') + '|---|',
  ];
  for (const r of results) {
    const cells = CHECK_IDS.map(id => { const c = r.checks.find(x => x.id === id); return c ? (c.pass ? '✅' : '❌') : '—'; });
    const note = r.error ? `error: ${String(r.error).slice(0, 80)}` : r.pageOverflow ? 'page-level 390px overflow (Known Issue)' : '';
    lines.push(`| ${r.ticker} | ${cells.join(' | ')} | ${note} |`);
  }
  const failures = results.flatMap(r => r.checks.filter(c => !c.pass).map(c => ({ ...c, ticker: r.ticker })));
  if (failures.length) {
    lines.push('', '## Failures', '');
    for (const f of failures) lines.push(`- **${f.ticker} ${f.id} ${f.name}**: expected ${f.expected}; got ${f.actual}`);
  }
  lines.push('', '## Checks', '', ...CHECK_IDS.map(id => `- ${id}: ${NAMES[id]}`), '', '*Generated by frontend/scripts/ui-verify-checklist.js*');
  const reportPath = path.join(outputDir, 'REPORT.md');
  fs.writeFileSync(reportPath, lines.join('\n'));
  console.log(`\nReport: ${reportPath}`);
}

function stamp() {
  const d = new Date();
  const p = (n) => String(n).padStart(2, '0');
  return `${d.getFullYear()}${p(d.getMonth() + 1)}${p(d.getDate())}-${p(d.getHours())}${p(d.getMinutes())}`;
}

async function main() {
  console.log('=== Analyze Page Verifier ===\n');
  const { tickers } = parseArgs();
  console.log(`Tickers: ${tickers.join(', ')}`);
  console.log('\nChecking services...');
  if (!(await checkServices())) {
    console.error('\nStart both services first (./start.sh).');
    process.exit(1);
  }

  // Same formatters/describer the card uses (GR59); ESM, so dynamic import.
  const mb = await import(path.resolve(__dirname, '../src/utils/marketBackdrop.js'));
  const kl = await import(path.resolve(__dirname, '../src/utils/keyLevels.js'));
  const dsv = await import(path.resolve(__dirname, '../src/utils/dataSourcesView.js'));
  const helpers = { describeMarketBackdrop: mb.describeMarketBackdrop, fmtPct: mb.fmtPct, fmtDate: mb.fmtDate, formatZoneRange: kl.formatZoneRange, providerLabel: dsv.providerLabel };

  let outputDir = path.resolve(__dirname, '../../docs/test', `UI_Verify_${stamp()}`);
  for (let n = 2; fs.existsSync(outputDir); n++) outputDir = outputDir.replace(/(_\d+)?$/, `_${n}`);
  fs.mkdirSync(outputDir, { recursive: true });

  const browser = await puppeteer.launch({ headless: 'shell', args: ['--no-sandbox'] });
  const results = [];
  try {
    const page = await browser.newPage();
    await page.setCacheEnabled(false);
    await page.setViewport({ width: 1440, height: 900 });
    for (let i = 0; i < tickers.length; i++) {
      results.push(await verifyTicker(page, tickers[i], i + 1, tickers.length, helpers));
      if (i < tickers.length - 1) await new Promise(r => setTimeout(r, BETWEEN_TICKERS_DELAY));
    }
  } finally {
    await browser.close();
  }

  generateReport(results, outputDir);
  const all = results.flatMap(r => r.checks);
  const failed = all.filter(c => !c.pass).length;
  console.log(`\n=== ${all.length - failed}/${all.length} checks passed ===`);
  process.exit(failed ? 1 : 0);
}

main().catch(err => { console.error('Fatal:', err); process.exit(1); });
