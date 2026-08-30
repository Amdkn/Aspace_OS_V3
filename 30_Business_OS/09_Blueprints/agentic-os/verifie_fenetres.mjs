/**
 * Verification des trois defauts signales : redimensionnement lateral, sortie
 * du cadre, bouton vert inerte. On pilote, on mesure, on ne suppose rien.
 */
import { pathToFileURL } from 'node:url';
import { homedir } from 'node:os';
import path from 'node:path';

const mod = await import(pathToFileURL(
  path.join(homedir(), 'gauntlet-eyes', 'node_modules', 'playwright', 'index.js')).href);
const chromium = mod.chromium ?? mod.default?.chromium;

const SORTIE = '/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/verif';
const dire = [];
const erreurs = [];

const b = await chromium.launch();
const p = await (await b.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
p.on('console', (m) => { if (m.type() === 'error') erreurs.push(m.text()); });
p.on('pageerror', (e) => erreurs.push(String(e)));

await p.goto('http://localhost:5199', { waitUntil: 'networkidle' });
await p.waitForTimeout(1500);

// Repart d'un bureau vide pour que la mesure soit reproductible.
await p.evaluate(() => { localStorage.clear(); indexedDB.deleteDatabase('agent-os'); });
await p.reload({ waitUntil: 'networkidle' });
await p.waitForTimeout(1800);

await p.locator('button[title]:has-text("Observateurs")').first().click();
await p.waitForTimeout(900);

const fenetre = p.locator('.window-chrome').first();
const geo = async () => {
  const bb = await fenetre.boundingBox();
  return { x: Math.round(bb.x), y: Math.round(bb.y), w: Math.round(bb.width), h: Math.round(bb.height) };
};

/* 1 · Bord DROIT — c'est celui qui ne repondait pas. */
let g0 = await geo();
await p.mouse.move(g0.x + g0.w - 3, g0.y + g0.h / 2);
await p.mouse.down();
await p.mouse.move(g0.x + g0.w + 160, g0.y + g0.h / 2, { steps: 12 });
await p.mouse.up();
await p.waitForTimeout(400);
let g1 = await geo();
dire.push(`${g1.w > g0.w + 80 ? 'OK   ' : 'ECHEC'}  bord droit — largeur ${g0.w} -> ${g1.w}`);

/* 2 · Bord GAUCHE. */
g0 = await geo();
await p.mouse.move(g0.x + 3, g0.y + g0.h / 2);
await p.mouse.down();
await p.mouse.move(g0.x - 120, g0.y + g0.h / 2, { steps: 12 });
await p.mouse.up();
await p.waitForTimeout(400);
g1 = await geo();
dire.push(`${g1.w > g0.w + 60 ? 'OK   ' : 'ECHEC'}  bord gauche — largeur ${g0.w} -> ${g1.w}`);

/* 3 · Sortie du cadre : on tire loin a droite, la fenetre doit rester dedans. */
g0 = await geo();
await p.mouse.move(g0.x + g0.w - 3, g0.y + g0.h / 2);
await p.mouse.down();
await p.mouse.move(3000, g0.y + g0.h / 2, { steps: 15 });
await p.mouse.up();
await p.waitForTimeout(400);
g1 = await geo();
const dedans = g1.x + g1.w <= 1445 && g1.x >= -5 && g1.y >= 25;
dire.push(`${dedans ? 'OK   ' : 'ECHEC'}  reste dans le cadre — x=${g1.x} w=${g1.w} (droite=${g1.x + g1.w})`);
await p.screenshot({ path: `${SORTIE}/f1-apres-redimensionnement.png` });

/* 4 · Bouton vert : plein ecran, puis retour a la taille d'avant. */
const avant = await geo();
await p.locator('button[aria-label="plein ecran"]').first().click();
await p.waitForTimeout(600);
const plein = await geo();
// On compare l'AIRE, pas la largeur : une fenetre deja pleine largeur ne peut
// pas s'elargir, et le test accusait le bouton a tort.
const aire = (g) => g.w * g.h;
dire.push(`${aire(plein) > aire(avant) * 1.2 ? 'OK   ' : 'ECHEC'}  bouton vert agrandit — ${avant.w}x${avant.h} -> ${plein.w}x${plein.h}`);
await p.screenshot({ path: `${SORTIE}/f2-plein-ecran.png` });

await p.locator('button[aria-label="restaurer"]').first().click();
await p.waitForTimeout(600);
const revenu = await geo();
const ok = Math.abs(revenu.w - avant.w) < 12 && Math.abs(revenu.h - avant.h) < 12;
dire.push(`${ok ? 'OK   ' : 'ECHEC'}  bouton vert restaure — ${plein.w}x${plein.h} -> ${revenu.w}x${revenu.h}`);

await b.close();
console.log(dire.join('\n'));
console.log('\nERREURS CONSOLE : ' + (erreurs.length || 'aucune'));
for (const e of erreurs.slice(0, 5)) console.log('  ' + e);
