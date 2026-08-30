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
const logs = [];
page.on('console', (m) => logs.push(`${m.type()}: ${m.text()}`));
await page.goto('http://localhost:5177', { waitUntil: 'networkidle' });
await page.waitForTimeout(3000);
const debug = await page.evaluate(() => ({
  keys: Object.keys(window.__coachos ?? {}),
}));
console.log('keys:', debug.keys);
console.log('logs matching [themes.store]:', logs.filter(l => l.includes('themes.store')));
await navigateur.close();
