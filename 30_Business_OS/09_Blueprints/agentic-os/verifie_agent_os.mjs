/**
 * Verification fonctionnelle d'Agent OS V1 — on pilote l'interface, on ne relit
 * pas le code. Les selecteurs passent par le TEXTE visible : la premiere version
 * cherchait `footer button` alors que le dock est un `div`, et declarait a tort
 * l'application cassee. Un test qui se trompe de selecteur accuse le mauvais
 * coupable.
 */
import { pathToFileURL } from 'node:url';
import { homedir } from 'node:os';
import path from 'node:path';

const mod = await import(pathToFileURL(
  path.join(homedir(), 'gauntlet-eyes', 'node_modules', 'playwright', 'index.js')).href);
const chromium = mod.chromium ?? mod.default?.chromium;

const URL_APP = 'http://localhost:5199';
const SORTIE = '/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/verif';

const erreurs = [], verdicts = [];
const dire = (n, ok, d = '') => verdicts.push(`${ok ? 'OK   ' : 'ECHEC'}  ${n}${d ? ' — ' + d : ''}`);

const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, acceptDownloads: true });
const p = await ctx.newPage();
p.on('console', (m) => { if (m.type() === 'error') erreurs.push(m.text()); });
p.on('pageerror', (e) => erreurs.push(String(e)));

await p.goto(URL_APP, { waitUntil: 'networkidle' });
await p.waitForTimeout(1500);

// Compte les fenetres : un panneau positionne en absolu, enfant direct du bureau.
const compterFenetres = () => p.evaluate(() =>
  [...document.querySelectorAll('div')].filter((d) => {
    const s = getComputedStyle(d);
    return s.position === 'absolute' && d.offsetWidth > 250 && d.offsetHeight > 150;
  }).length);

const dock = (nom) => p.locator(`button[title]:has-text("${nom}")`).first();

dire('dock peuple', (await p.locator('button[title]').count()) >= 3,
     `${await p.locator('button[title]').count()} boutons titres`);

await dock('Observateurs').click(); await p.waitForTimeout(900);
const n1 = await compterFenetres();
dire('une fenetre s ouvre', n1 >= 1, `${n1} panneau(x)`);

await dock('Memoires').click().catch(async () => { await dock('moires').click(); });
await p.waitForTimeout(500);
await dock('Memoires').click().catch(async () => { await dock('moires').click(); });
await p.waitForTimeout(900);
const n2 = await compterFenetres();
dire('multi-instances', n2 > n1, `${n1} -> ${n2}`);
await p.screenshot({ path: `${SORTIE}/01-fenetres.png` });

await p.reload({ waitUntil: 'networkidle' }); await p.waitForTimeout(2200);
const n3 = await compterFenetres();
dire('persistance au rechargement', n3 >= 1, `${n2} avant, ${n3} apres`);
await p.screenshot({ path: `${SORTIE}/02-apres-rechargement.png` });

let exp = false, nom = '';
const menus = p.locator('button:has-text("Fichier"), button:has-text("Agent OS")');
for (let i = 0; i < (await menus.count()) && !exp; i++) {
  await menus.nth(i).click().catch(() => {});
  await p.waitForTimeout(400);
  const item = p.locator('text=/export|instantan|snapshot|sauvegard/i').first();
  if (await item.count()) {
    const dl = p.waitForEvent('download', { timeout: 9000 }).catch(() => null);
    await item.click().catch(() => {});
    const d = await dl;
    if (d) { exp = true; nom = d.suggestedFilename(); }
  }
  await p.keyboard.press('Escape').catch(() => {});
}
dire('export d instantane', exp, nom || 'aucun telechargement');
await p.screenshot({ path: `${SORTIE}/03-final.png` });
await b.close();

console.log(verdicts.join('\n'));
console.log('\nERREURS CONSOLE : ' + (erreurs.length || 'aucune'));
for (const e of erreurs.slice(0, 5)) console.log('  ' + e);
