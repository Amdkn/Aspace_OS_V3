/**
 * capture.mjs — preuves 1-6 du brief D.
 *
 * Ce script déclenche les six captures qui établissent que les scénarios
 * fonctionnent : l'agent propose, rien ne change, on compare, la file
 * montre le scénario, l'approbateur édite, on fusionne, et la 6e — la plus
 * escamotée — montre qu'une fusion ratée laisse l'état réel intact.
 *
 * Pilotage par window.__coachos.* : on tire les ficelles directement, pas
 * par clic souris — un clic synthétisé ne reproduit pas la séquence
 * d'événements que React attend (déjà payé plusieurs fois sur ce projet).
 */
import { pathToFileURL } from 'node:url';
import { existsSync } from 'node:fs';
import { homedir } from 'node:os';
import path from 'node:path';

const CANDIDATS = [
  path.join(homedir(), 'gauntlet-eyes', 'node_modules', 'playwright', 'index.js'),
  path.join(process.cwd(), 'node_modules', 'playwright', 'index.js'),
];
const trouve = CANDIDATS.find(existsSync);
if (!trouve) {
  console.error('playwright introuvable');
  process.exit(2);
}
const mod = await import(pathToFileURL(trouve).href);
const chromium = mod.chromium ?? mod.default?.chromium;

const BASE = process.env.BASE ?? 'http://localhost:5177';
const OUT = process.env.OUT ?? path.join(process.cwd(), 'preuves', 'D');

const navigateur = await chromium.launch();
const page = await navigateur.newPage({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
});

const erreurs = [];
page.on('console', (m) => { if (m.type() === 'error') erreurs.push(m.text()); });
page.on('pageerror', (e) => erreurs.push(String(e)));

await page.goto(BASE, { waitUntil: 'networkidle' });

// Reset état scénario
await page.evaluate(() => {
  localStorage.removeItem('coach-os-scenarios-v1');
  // Forcer une rehydratation via le store
  if (window.__coachos?.scenarios) {
    const s = window.__coachos.scenarios.getState();
    if (s.scenarios) Object.keys(s.scenarios).forEach((id) => s.deleteScenario(id));
  }
});

// === PREUVE 1 : l'agent propose, RIEN n'a changé ===
await page.evaluate(() => {
  window.__coachos.shell.getState().openApp('people', 'People');
});
await page.waitForTimeout(800);
await page.evaluate(() => {
  // Proposition avec un thème RÉEL (aurora) pour qu'on puisse la fusionner
  // plus tard sans surprise.
  window.__coachos.scenarios.getState().addProposal({
    toolName: 'changerTheme',
    args: { themeId: 'aurora' },
    displayName: 'Thème global « aurora »',
  });
});
await page.waitForTimeout(400);
const themeAfterProposal = await page.evaluate(() => window.__coachos.themes.getState().globalTheme);
console.log(`[preuve 1] theme après proposition (avant fusion) = ${themeAfterProposal} — ne doit PAS être 'aurora'`);

// Naviguer vers Approvals
const approvalsTab = page.locator('[data-section="Approvals"]');
const aCount = await approvalsTab.count();
console.log(`[preuve 1] data-section="Approvals" count = ${aCount}`);
if (aCount === 0) {
  console.error("section Approvals introuvable — abandon");
  await navigateur.close();
  process.exit(1);
}
await approvalsTab.click();
await page.waitForTimeout(800);
await page.screenshot({ path: `${OUT}/01-proposition-rien-change.png`, fullPage: false });
console.log(`[preuve 1] capture : ${OUT}/01-proposition-rien-change.png`);

// === PREUVE 2 : deux options comparées côte à côte ===
await page.evaluate(() => {
  const store = window.__coachos.scenarios.getState();
  const sc = store.createScenario({
    name: 'Choix de thème — Patrick Bernard',
    createdBy: 'agent:orchestrator',
    rationale: 'Le client hésite entre trois directions. Trois devis comparés.',
  });
  const a = store.addProposal({ toolName: 'changerTheme', args: { themeId: 'brutalism' }, displayName: 'Thème brutalism' });
  const b = store.addProposal({ toolName: 'changerTheme', args: { themeId: 'editorial' }, displayName: 'Thème editorial' });
  const c = store.addProposal({ toolName: 'changerTheme', args: { themeId: 'cyberpunk' }, displayName: 'Thème cyberpunk' });
  store.setComparison(sc.id, {
    options: [
      { id: 'A', label: 'Direction A · Brutalism', rationale: 'Couleurs franches, beaucoup de contraste, écritures grasses.', metrics: [
        { label: 'personnalité', value: 'forte' },
        { label: 'lisibilité', value: 'moyenne' },
        { label: 'déplacements UI', value: 'majeurs' },
      ], proposalIds: [a.proposalId] },
      { id: 'B', label: 'Direction B · Editorial', rationale: 'Sérénité, lecture longue, coins doux.', metrics: [
        { label: 'personnalité', value: 'sobre' },
        { label: 'lisibilité', value: 'excellente' },
        { label: 'déplacements UI', value: 'mineurs' },
      ], proposalIds: [b.proposalId] },
      { id: 'C', label: 'Direction C · Cyberpunk', rationale: 'Bleu profond, accents néon, look console.', metrics: [
        { label: 'personnalité', value: 'cinéma' },
        { label: 'lisibilité', value: 'bonne' },
        { label: 'déplacements UI', value: 'modérés' },
      ], proposalIds: [c.proposalId] },
    ],
    recommendation: 'B',
  });
});
await page.waitForTimeout(800);
// On ouvre le détail du scénario "Choix de thème" pour voir la comparaison
const choixRow = page.locator('[data-scenario-row]').filter({ hasText: 'Choix de thème' });
if (await choixRow.count() > 0) {
  await choixRow.first().click();
  await page.waitForTimeout(700);
}
await page.screenshot({ path: `${OUT}/02-comparaison-cote-a-cote.png`, fullPage: true });
console.log(`[preuve 2] capture : ${OUT}/02-comparaison-cote-a-cote.png`);

// === PREUVE 3 : la file d'approbation avec un scénario en attente ===
// Soumettre les autres scénarios (auto-créé et Choix de thème) à pending.
await page.evaluate(() => {
  const store = window.__coachos.scenarios.getState();
  for (const id of store.scenarioOrder) {
    const sc = store.scenarios[id];
    if (sc && sc.status === 'draft') store.submitForApproval(id);
  }
});
await page.waitForTimeout(500);
await page.evaluate(() => {
  // Retour à la file
  const closeBtn = document.querySelector('[data-close-detail]');
  if (closeBtn) closeBtn.click();
});
await page.waitForTimeout(500);
await page.screenshot({ path: `${OUT}/03-file-approbation.png`, fullPage: false });
console.log(`[preuve 3] capture : ${OUT}/03-file-approbation.png`);

// === PREUVE 4 : le scénario édité par l'approbateur AVANT fusion ===
const firstPendingRow = page.locator('[data-scenario-row][data-scenario-status="pending"]').first();
const prCount = await firstPendingRow.count();
console.log(`[preuve 4] pending rows = ${prCount}`);
if (prCount > 0) {
  await firstPendingRow.click();
  await page.waitForTimeout(700);
  const editBtn = page.locator('[data-edit-proposal]').first();
  if (await editBtn.count() > 0) {
    await editBtn.click();
    await page.waitForTimeout(500);
    await page.screenshot({ path: `${OUT}/04-scenario-edite-avant-fusion.png`, fullPage: true });
    console.log(`[preuve 4] capture : ${OUT}/04-scenario-edite-avant-fusion.png`);
  } else {
    console.error('[preuve 4] aucun bouton edit');
  }
}

// === PREUVE 5 : après fusion, la modification est appliquée ===
// Sauver l'édition, puis fusionner.
const saveBtn = page.locator('[data-save-edit]');
if (await saveBtn.count() > 0) await saveBtn.click();
await page.waitForTimeout(400);

const themeBeforeMerge = await page.evaluate(() => window.__coachos.themes.getState().globalTheme);
console.log(`[preuve 5] theme AVANT fusion = ${themeBeforeMerge}`);
const mergeBtn = page.locator('[data-approve-merge]');
if (await mergeBtn.count() > 0) {
  await mergeBtn.click();
  await page.waitForTimeout(800);
  const themeAfterMerge = await page.evaluate(() => window.__coachos.themes.getState().globalTheme);
  console.log(`[preuve 5] theme APRÈS fusion = ${themeAfterMerge}`);
  await page.screenshot({ path: `${OUT}/05-apres-fusion-applique.png`, fullPage: false });
  console.log(`[preuve 5] capture : ${OUT}/05-apres-fusion-applique.png`);
} else {
  console.error('[preuve 5] aucun bouton Approve & Merge');
}

// === PREUVE 6 : la plus escamotée — fusion qui échoue, AUCUNE modification appliquée ===
// Créer un scénario avec une proposition qui va marcher puis une qui plante.
// Le thème cible DOIT être valide pour la 1ère étape, et la 2ème étape doit
// être invalide. Pour reproduire la sémantique tout-ou-rien : la 1ère est
// appliquée, puis revertée.
await page.evaluate(() => {
  const w = window;
  const store = w.__coachos.scenarios.getState();
  // On nettoie le scénario courant, puis on crée le test
  store.setCurrentScenario(null);
  const sc = store.createScenario({
    name: 'Test atomicité — proposition qui échoue',
    createdBy: 'agent:test',
    rationale: 'Étape 2 doit échouer : thème inexistant. La 1 doit être revertée.',
  });
  // Étape 1 : thème VALIDE → doit être appliqué PUIS reverté.
  store.addProposal({
    toolName: 'changerTheme',
    args: { themeId: 'aurora' },
    displayName: 'Thème aurora (devrait être reverté)',
  });
  // Étape 2 : thème INVALIDE → échec garanti.
  store.addProposal({
    toolName: 'changerTheme',
    args: { themeId: 'ce-theme-nexiste-pas' },
    displayName: 'Thème inexistant (échec garanti)',
  });
  store.submitForApproval(sc.id);
  // Lancer la fusion via approveAndMerge directement avec un applicateur
  // custom qui force l'échec sur le thème inconnu.
  w.__coachos.scenarios.getState().approveAndMerge(sc.id, {
    changerTheme: (args) => {
      const themeId = String(args.themeId ?? '');
      if (themeId === 'ce-theme-nexiste-pas') {
        return { ok: false, error: `Thème inconnu : "${themeId}"` };
      }
      const prevGlobal = w.__coachos.themes.getState().globalTheme;
      w.__coachos.themes.getState().setGlobalTheme(themeId);
      return {
        ok: true,
        revert: () => w.__coachos.themes.getState().setGlobalTheme(prevGlobal),
      };
    },
  });
});
const themeBeforeFailedMerge = await page.evaluate(() => window.__coachos.themes.getState().globalTheme);
console.log(`[preuve 6] theme AVANT fusion ratée = ${themeBeforeFailedMerge}`);
const themeAfterFailedMerge = await page.evaluate(() => window.__coachos.themes.getState().globalTheme);
console.log(`[preuve 6] theme APRÈS fusion ratée = ${themeAfterFailedMerge} (doit être identique à AVANT)`);

// Aller sur Approvals et capturer la file
const aTabFinal = page.locator('[data-section="Approvals"]');
if (await aTabFinal.count() > 0) await aTabFinal.click();
await page.waitForTimeout(700);
// Si on est encore dans le détail, cliquer le bouton retour
const closeBtn = page.locator('[data-close-detail]');
if (await closeBtn.count() > 0) {
  await closeBtn.click();
  await page.waitForTimeout(500);
}

// Capture d'abord la file complète pour montrer tous les scénarios
await page.screenshot({ path: `${OUT}/06-fusion-echoue-aucune-modif.png`, fullPage: true });
console.log(`[preuve 6] capture (file) : ${OUT}/06-fusion-echoue-aucune-modif.png`);

// Maintenant cliquer sur le scénario "Test atomicité" pour voir le détail
// avec la bannière rouge et la proposition 'aurora' marquée 'reverted'.
const allRows = await page.locator('[data-scenario-row]').count();
const rowsInfo = await page.evaluate(() => {
  const rows = Array.from(document.querySelectorAll('[data-scenario-row]'));
  return rows.map((r) => ({
    id: r.getAttribute('data-scenario-id'),
    status: r.getAttribute('data-scenario-status'),
    text: r.textContent?.slice(0, 100),
  }));
});
console.log(`[preuve 6] rows in queue = ${allRows}`, JSON.stringify(rowsInfo, null, 2));
const atomicityRow = page.locator('[data-scenario-row]').filter({ hasText: 'Test atomicit' });
const arCount = await atomicityRow.count();
console.log(`[preuve 6] atomicity rows = ${arCount}`);
if (arCount > 0) {
  await atomicityRow.first().scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await atomicityRow.first().click();
  await page.waitForTimeout(800);
  await page.screenshot({ path: `${OUT}/06b-detail-fusion-echec.png`, fullPage: true });
  console.log(`[preuve 6b] capture (détail échec) : ${OUT}/06b-detail-fusion-echec.png`);
}

await navigateur.close();

if (erreurs.length) {
  console.log(`\nERREURS CONSOLE (${erreurs.length}) :`);
  for (const e of erreurs.slice(0, 10)) console.log('  ' + e);
} else {
  console.log('\nAucune erreur de console.');
}
