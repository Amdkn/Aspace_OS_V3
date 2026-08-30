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
await page.goto('http://localhost:5177', { waitUntil: 'networkidle' });
// Cliquer un bureau pour activer l'agent (charge tools.ts)
await page.evaluate(() => window.__coachos.shell.getState().openApp('people', 'People'));
await page.waitForTimeout(1500);
// Now look at what's on the page
const debug = await page.evaluate(() => ({
  keys: Object.keys(window.__coachos ?? {}),
  toolsKeys: window.__coachos.tools ? Object.keys(window.__coachos.tools) : null,
  themesLoaded: typeof window.__coachos.themes === 'object',
  globalTheme: window.__coachos.themes?.getState?.()?.globalTheme ?? null,
  appThemes: window.__coachos.themes?.getState?.()?.appThemes ?? null,
}));
console.log(JSON.stringify(debug, null, 2));
await navigateur.close();
