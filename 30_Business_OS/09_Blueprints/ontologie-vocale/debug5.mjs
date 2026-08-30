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
await page.waitForTimeout(4000);
const debug = await page.evaluate(() => {
  const w = window;
  const out = {
    keys: Object.keys(w.__coachos ?? {}),
    ownProps: Object.getOwnPropertyNames(w.__coachos ?? {}),
    themesType: typeof w.__coachos?.themes,
    toolsType: typeof w.__coachos?.tools,
    debug: 'no debug',
  };
  return out;
});
console.log(JSON.stringify(debug, null, 2));
console.log('all logs:', logs.filter(l => !l.includes('Re-optimizing') && !l.includes('optimizer')).slice(-20));
await navigateur.close();
