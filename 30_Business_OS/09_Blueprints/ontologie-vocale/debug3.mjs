import { pathToFileURL } from 'node:url';
import { existsSync } from 'node:fs';
import { homedir } from 'node:os';
import path from 'node:path';

const CANDIDATS = [
  path.join(homedir(), 'gauntlet-eyes', 'node_modules', 'playwright', 'index.js'),
];
const trouve = CANDIDATS.find(existsSync);
const mod = await import(pathToFileURL(trouve).href);
const chromium = mod.chromium ?? mod.default?.chromium;

const navigateur = await chromium.launch();
const page = await navigateur.newPage({ viewport: { width: 1440, height: 900 } });
const errors = [];
page.on('pageerror', (e) => errors.push(String(e)));
page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
await page.goto('http://localhost:5177', { waitUntil: 'networkidle' });
// Force reload to pick up vite updates
await page.reload({ waitUntil: 'networkidle' });
await page.waitForTimeout(2000);
const debug = await page.evaluate(() => ({
  keys: Object.keys(window.__coachos ?? {}),
  active: window.__coachos.assistant?.getState?.()?.active,
}));
console.log('after reload:', JSON.stringify(debug, null, 2));
// Open the agent by enabling it - if it's not active
await page.evaluate(() => {
  if (window.__coachos.assistant) {
    const s = window.__coachos.assistant.getState();
    if (!s.active) s.setActive(true);
  }
});
await page.waitForTimeout(2000);
const debug2 = await page.evaluate(() => ({
  keys: Object.keys(window.__coachos ?? {}),
  scenarios: window.__coachos.scenarios ? 'yes' : 'no',
  themes: typeof window.__coachos.themes === 'object',
  tools: typeof window.__coachos.tools === 'object',
}));
console.log('after assistant enable:', JSON.stringify(debug2, null, 2));
console.log('errors:', errors);
await navigateur.close();
