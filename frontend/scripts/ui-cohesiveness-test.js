#!/usr/bin/env node
/**
 * UI Cohesiveness Test Automation
 *
 * Automates the manual process of:
 * 1. Enter ticker in search
 * 2. Wait for analysis
 * 3. Scroll through all sections
 * 4. Save full-page PDF (Full Analysis view) for manual review
 *
 * Day 124 (Analyze Redesign Step 8): waits on the cards' data-testid hooks (the old
 * "Holding Period" wait timed out on every ticker), drops --holding/--all-periods
 * (selector removed Day 123) and the BUY/HOLD/AVOID + T:/F:/S:/R: scraping, and
 * emits a manual checklist for the current page. Automated checks live in
 * ui-verify-checklist.js.
 *
 * Usage:
 *   node scripts/ui-cohesiveness-test.js
 *   node scripts/ui-cohesiveness-test.js AAPL NVDA   # specific tickers
 *   node scripts/ui-cohesiveness-test.js --output MyFolder
 *
 * Prerequisites:
 *   - Backend running on http://localhost:5001
 *   - Frontend running on http://localhost:3000
 *   - npm install puppeteer (already in devDependencies)
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

// --- Configuration ---
const FRONTEND_URL = 'http://localhost:3000';
const BACKEND_HEALTH_URL = 'http://localhost:5001/api/health';

// Default diverse tickers covering multiple scenarios
const DEFAULT_TICKERS = [
  'AAPL',   // Large-cap tech, strong fundamentals
  'JNJ',    // Defensive/healthcare, high ADX
  'F',      // Cyclical, mixed signals (tests signal weighting)
  'COIN',   // Volatile crypto-adjacent
  'AFRM',   // Low TT score, weak tech (should be AVOID)
  'XOM',    // Energy, value play
  'PLTR',   // High-growth, expensive
  'VZ',     // Telecom/dividend, low ADX
  'SMCI',   // Volatile momentum
  'META',   // Mega-cap tech, strong RS
];

// Timeouts
const ANALYSIS_TIMEOUT = 60000;  // 60s max per ticker (API calls can be slow)
const PAGE_LOAD_TIMEOUT = 15000;
const BETWEEN_TICKERS_DELAY = 3000; // 3s between tickers to avoid rate limiting

// --- Parse CLI arguments ---
function parseArgs() {
  const args = process.argv.slice(2);
  let tickers = [];
  let outputDir = null;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--holding' || args[i] === '--all-periods') {
      console.error(`${args[i]}: removed Day 123 with the Holding Period selector.`);
      process.exit(2);
    } else if (args[i] === '--output' && args[i + 1]) {
      outputDir = args[i + 1];
      i++;
    } else if (args[i].startsWith('--')) {
      console.error(`Unknown option: ${args[i]}`);
      process.exit(2);
    } else {
      tickers.push(args[i].toUpperCase());
    }
  }

  if (tickers.length === 0) tickers = [...DEFAULT_TICKERS];

  return { tickers, outputDir };
}

// --- Ensure output directory exists ---
function setupOutputDir(customDir) {
  const timestamp = new Date().toISOString().slice(0, 10).replace(/-/g, '');
  const dirName = customDir || `UI_Cohesiveness_Test_${timestamp}`;
  const outputPath = path.resolve(__dirname, '../../docs/test', dirName);

  if (!fs.existsSync(outputPath)) {
    fs.mkdirSync(outputPath, { recursive: true });
  }
  return outputPath;
}

// --- Check services are running ---
async function checkServices() {
  const http = require('http');

  // Check backend
  try {
    await new Promise((resolve, reject) => {
      http.get(BACKEND_HEALTH_URL, (res) => {
        if (res.statusCode === 200) resolve();
        else reject(new Error(`Backend returned ${res.statusCode}`));
      }).on('error', reject);
    });
    console.log('  Backend: OK (localhost:5001)');
  } catch {
    console.error('  Backend: NOT RUNNING - start with ./start.sh backend');
    return false;
  }

  // Check frontend
  try {
    await new Promise((resolve, reject) => {
      http.get(FRONTEND_URL, (res) => {
        if (res.statusCode === 200) resolve();
        else reject(new Error(`Frontend returned ${res.statusCode}`));
      }).on('error', reject);
    });
    console.log('  Frontend: OK (localhost:3000)');
  } catch {
    console.error('  Frontend: NOT RUNNING - start with ./start.sh');
    return false;
  }

  return true;
}

// --- Analyze a single ticker and save PDF ---
async function analyzeTicker(page, ticker, outputDir, index, total) {
  const label = `[${index}/${total}] ${ticker}`;
  const pdfFilename = `${ticker}.pdf`;
  const pdfPath = path.join(outputDir, pdfFilename);

  console.log(`\n${label}: Starting analysis...`);

  try {
    // Clear previous results - navigate fresh
    await page.goto(FRONTEND_URL, { waitUntil: 'networkidle2', timeout: PAGE_LOAD_TIMEOUT });
    await page.waitForSelector('input[placeholder*="ticker"]', { timeout: 5000 });

    // Type ticker and press Enter to trigger analysis
    const input = await page.$('input[placeholder*="ticker"]');
    await input.click({ clickCount: 3 }); // Select all existing text
    await input.type(ticker, { delay: 50 });
    await page.keyboard.press('Enter');
    console.log(`${label}: Submitted, waiting for results...`);

    // Wait for the Full Analysis cards (default view since Day 124) or the error banner.
    await page.waitForSelector('[data-testid="card-technical-read"], [data-testid="analysis-error"]', { timeout: ANALYSIS_TIMEOUT });
    try { await page.waitForNetworkIdle({ idleTime: 1000, timeout: 30000 }); }
    catch { console.warn(`${label}: network still busy after 30s; capturing anyway`); }

    const errorText = await page.evaluate(() => {
      const el = document.querySelector('[data-testid="analysis-error"]');
      return el ? el.textContent : null;
    });
    const hasError = !!errorText;

    if (hasError) {
      console.log(`${label}: API ERROR - ${errorText.slice(0, 100)}`);

      // Still save PDF of error state
      await page.pdf({ path: pdfPath, format: 'A4', printBackground: true });
      return { ticker, status: 'error', error: errorText.slice(0, 100), pdf: pdfFilename };
    }

    // Page facts from the card hooks (no class-name scraping).
    const pageData = await page.evaluate(() => {
      const t = (sel) => { const el = document.querySelector(`[data-testid="${sel}"]`); return el ? el.textContent.replace(/\s+/g, ' ').trim() : null; };
      const header = document.querySelector('[data-testid="card-stock-header"]');
      const h2 = header ? header.querySelector('h2') : null;
      const cards = [...document.querySelectorAll('[data-testid^="card-"]')].map(el => el.dataset.testid.replace('card-', ''));
      return { tickerName: h2 ? h2.textContent.trim() : null, classification: header && header.querySelector('p') ? header.querySelector('p').innerText.replace(/\s+/g, ' ').trim().slice(0, 80) : null, cards };
    });
    // Simple view badge: toggle, read, toggle back so the PDF is the Full view.
    pageData.simpleBadge = await page.evaluate(async () => {
      const click = (lbl) => { const b = [...document.querySelectorAll('button')].find(x => x.textContent.trim() === lbl); if (b) b.click(); return !!b; };
      if (!click('✅ Simple Checklist (9 criteria)')) return null;
      await new Promise(r => setTimeout(r, 400));
      const el = document.querySelector('[data-testid="card-simple-verdict"]');
      const text = el ? el.innerText.replace(/\s+/g, ' ').trim() : null;
      click('Full Analysis');
      await new Promise(r => setTimeout(r, 400));
      return text;
    });

    console.log(`${label}: ${pageData.tickerName || ticker} | ${pageData.classification || ''} | Simple: ${pageData.simpleBadge || 'N/A'} | cards: ${pageData.cards.join(', ')}`);

    // Scroll to bottom to ensure all lazy content loads
    await page.evaluate(async () => {
      await new Promise((resolve) => {
        let totalHeight = 0;
        const distance = 300;
        const timer = setInterval(() => {
          window.scrollBy(0, distance);
          totalHeight += distance;
          if (totalHeight >= document.body.scrollHeight) {
            clearInterval(timer);
            resolve();
          }
        }, 100);
      });
    });
    await new Promise(r => setTimeout(r, 500));

    // Scroll back to top
    await page.evaluate(() => window.scrollTo(0, 0));
    await new Promise(r => setTimeout(r, 300));

    // Save PDF (full page)
    await page.pdf({
      path: pdfPath,
      format: 'A4',
      printBackground: true,
      margin: { top: '10mm', bottom: '10mm', left: '10mm', right: '10mm' },
    });

    console.log(`${label}: Saved ${pdfFilename}`);
    return {
      ticker,
      status: 'success',
      name: pageData.tickerName,
      classification: pageData.classification,
      simpleBadge: pageData.simpleBadge,
      cards: pageData.cards,
      pdf: pdfFilename
    };

  } catch (err) {
    console.error(`${label}: FAILED - ${err.message}`);
    // Try to save whatever state we're in
    try {
      await page.pdf({ path: pdfPath, format: 'A4', printBackground: true });
    } catch { /* ignore */ }
    return { ticker, status: 'failed', error: err.message, pdf: pdfFilename };
  }
}

// --- Generate summary report ---
function generateReport(results, outputDir, config) {
  const timestamp = new Date().toISOString();
  const lines = [
    `# UI Cohesiveness Test Report`,
    ``,
    `**Date:** ${timestamp}`,
    `**Tickers Tested:** ${config.tickers.length}`,
    `**Total PDFs Generated:** ${results.filter(r => r.pdf).length}`,
    ``,
    `---`,
    ``,
    `## Results Summary`,
    ``,
    `| # | Ticker | Name | Classification | Simple view | Cards | Status | PDF |`,
    `|---|--------|------|----------------|-------------|-------|--------|-----|`,
  ];

  results.forEach((r, i) => {
    lines.push(
      `| ${i + 1} | ${r.ticker} | ${r.name || ''} | ${r.classification || ''} | ${r.simpleBadge || 'N/A'} | ${(r.cards || []).length} | ${r.status}${r.error ? `: ${r.error}` : ''} | ${r.pdf || 'none'} |`
    );
  });

  lines.push('', '---', '');
  lines.push('## Checklist (Manual Review)');
  lines.push('');
  lines.push('For each PDF, verify:');
  lines.push('- [ ] Market backdrop is the first card and shows facts only (no Favorable/Unfavorable label)');
  lines.push('- [ ] No BUY/HOLD/AVOID verdict anywhere; the Simple view says TRADE or No Trade');
  lines.push('- [ ] Each card says what its read is based on (rules, data source, dates)');
  lines.push('- [ ] Anything that could not load says so plainly; no blank or made-up values');
  lines.push('- [ ] An ETF says "Exchange-traded fund (ETF)", never "Unknown"');
  lines.push('- [ ] Earnings date (Fundamentals) and header badge agree');
  lines.push('- [ ] Trade Setup stop/target come from real support/resistance, or the card says why not');
  lines.push('');
  lines.push('Automated checks: `node scripts/ui-verify-checklist.js`.');
  lines.push('');

  const reportPath = path.join(outputDir, 'TEST_REPORT.md');
  fs.writeFileSync(reportPath, lines.join('\n'));
  console.log(`\nReport saved: ${reportPath}`);
}

// --- Main ---
async function main() {
  console.log('=== UI Cohesiveness Test Automation ===\n');

  const config = parseArgs();
  console.log(`Tickers: ${config.tickers.join(', ')}`);

  // Check services
  console.log('\nChecking services...');
  const servicesOk = await checkServices();
  if (!servicesOk) {
    console.error('\nPlease start both backend and frontend first.');
    process.exit(1);
  }

  // Setup output
  const outputDir = setupOutputDir(config.outputDir);
  console.log(`\nOutput directory: ${outputDir}`);

  // Launch browser
  console.log('\nLaunching browser...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });

  // Emulate print media for better PDF output
  await page.emulateMediaType('screen');

  const results = [];
  const totalTests = config.tickers.length;
  let testNum = 0;

  for (const ticker of config.tickers) {
    testNum++;
    const result = await analyzeTicker(page, ticker, outputDir, testNum, totalTests);
    results.push(result);

    // Delay between tickers to avoid rate limiting
    if (testNum < totalTests) {
      console.log(`  Waiting ${BETWEEN_TICKERS_DELAY / 1000}s before next ticker...`);
      await new Promise(r => setTimeout(r, BETWEEN_TICKERS_DELAY));
    }
  }

  // Generate report
  generateReport(results, outputDir, config);

  // Summary
  console.log('\n=== Test Complete ===');
  const success = results.filter(r => r.status === 'success').length;
  const errors = results.filter(r => r.status === 'error').length;
  const failed = results.filter(r => r.status === 'failed').length;
  console.log(`  Success: ${success}/${totalTests}`);
  if (errors) console.log(`  Errors: ${errors}`);
  if (failed) console.log(`  Failed: ${failed}`);
  console.log(`  PDFs saved to: ${outputDir}`);

  await browser.close();
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
