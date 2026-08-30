import { pathToFileURL } from 'node:url';
import { existsSync } from 'node:fs';
import { homedir } from 'node:os';
import path from 'node:path';

const CANDIDATS = [
  path.join(homedir(), 'gauntlet-eyes', 'node_modules', 'playwright', 'index.js'),
  path.join(process.cwd(), 'node_modules', 'playwright', 'index.js'),
];
const trouve = CANDIDATS.find(existsSync);
const mod = await import(pathToFileURL(trouve).href);
const chromium = mod.chromium ?? mod.default?.chromium;

const navigateur = await chromium.launch();
const page = await navigateur.newPage({ viewport: { width: 1440, height: 900 } });
await page.goto('http://localhost:5177', { waitUntil: 'networkidle' });
// Ouvrir People pour charger le theme store
await page.evaluate(() => window.__coachos.shell.getState().openApp('people', 'People'));
await page.waitForTimeout(2000);
const keys = await page.evaluate(() => Object.keys(window.__coachos ?? {}));
console.log('window.__coachos keys:', keys);
await navigateur.close();
