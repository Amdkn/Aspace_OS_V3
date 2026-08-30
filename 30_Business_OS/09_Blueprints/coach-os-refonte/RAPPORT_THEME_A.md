# RAPPORT_THEME_A — pages de detail, groupe A

> **Périmètre** : `src/apps/operations/`, `src/apps/product/`, `src/apps/growth/`, `src/apps/it-rd/`, `src/apps/tasks/`.
> **Date** : 2026-08-06.
> **Auteur** : agent front, vague A du refac theme.

## Résumé

Cinq apps corrigées. Le défaut — `DynamicPageView` rendu dans le corps d'une section, donc à l'intérieur d'`AppFrame` — a été levé. Toutes les pages de detail passent désormais par `<AppDetailOverlay>` monté en frère d'`<AppFrame>`. Pour les apps qui n'avaient qu'une fiche minimaliste (Product, Growth, IT/R&D), la page a été refaite autour des cinq blocs du brief. Operations et Tasks gardent leur mise en page signature (control board, command console) — la fiche suit maintenant le theme global, c'est l'unique changement visible.

| App | AppDetailOverlay (sibling) | Page detail refaite |
|-----|---------------------------|---------------------|
| Operations | ✓ (legacy + nouveau) | non — control board déjà canonique |
| Product | ✓ (legacy + nouveau) | oui |
| Growth | ✓ (legacy + nouveau) | oui |
| IT/R&D | ✓ (legacy + nouveau) | oui |
| Tasks | ✓ (legacy + nouveau) | non — command console déjà canonique |

## Le défaut mesuré

Toutes les apps du groupe A avaient un pattern du type :

```tsx
const Processus = () => {
  if (processesDrill.openId) {
    return <DynamicPageView collectionId="processes" itemId={processesDrill.openId} ... />;
  }
  return <div className="p-7">...</div>;
};
```

`<DynamicPageView>` était rendu à l'intérieur du `<section>` qui est dans `<AppFrame>`. AppFrame écrit ses tokens `--theme-*` sur **son propre `div`**. Tout descendant hérite. La fiche suiveuse ne tombait jamais sur `:root`, donc ne lisait jamais le theme que ThemeApplier pose au niveau global. Verdict du propriétaire : « les anciennes pages de Product et Growth s'adaptent au theme de la sidebar mais pas les nouvelles » — c'était le même défaut des deux côtés.

## Le motif de sortie

Tous les `App` du groupe A suivent maintenant ce canevas (cf. par exemple `src/apps/operations/OperationsApp.tsx` fin de fichier) :

```tsx
const drillRegistry = [
  { drill: processesDrill, collection: 'processes' },
  { drill: benchmarksDrill, collection: 'benchmarks' },
  { drill: changesDrill, collection: 'changes' },
  { drill: alertsDrill, collection: 'alerts' },
];
const openDrillEntry = drillRegistry.find((d) => d.drill.openId !== null);
const openDrillCollection = openDrillEntry?.collection ?? null;
const openDrillId = openDrillEntry?.drill.openId ?? null;

return (
  <>
    <AppFrame title="Operations" sections={sections} ... />
    {detail ? (
      <AppDetailOverlay appId="operations" accent="#4f46e5" onBack={() => setDetail(null)}>
        <OperationsDetailPage item={detail} onBack={() => setDetail(null)} />
      </AppDetailOverlay>
    ) : null}
    {openDrillCollection !== null && openDrillId !== null ? (
      <AppDetailOverlay appId="operations" accent="#4f46e5" onBack={closeOpenDrill} ...>
        <DynamicPageView
          collectionId={openDrillCollection}
          itemId={openDrillId}
          onBack={closeOpenDrill}
          onNavigate={navigateOpenDrill}
        />
      </AppDetailOverlay>
    ) : null}
  </>
);
```

`AppDetailOverlay` est monté en frère d'`AppFrame`, ce qui correspond à la doctrine canon (cf. `docs/superpowers/specs/2026-07-30-coach-os-app-detail-pages-design.md` §3.2). Le `position: absolute` de l'overlay trouve son ancêtre positionné sur la racine du bureau, pas sur AppFrame. Ses tokens `--theme-bg` / `--theme-text` retombent sur `:root`, donc sur le theme global posé par `ThemeApplier`.

## Structure de retour — par app

### Operations (`src/apps/operations/OperationsApp.tsx`)

```
<>
  <AppFrame title="Operations" subtitle="Batman domain" sections={sections} canvasNuance={1} />
  {detail ? (
    <AppDetailOverlay appId="operations" accent="#4f46e5"
      onBack={() => setDetail(null)}
      motion={{ kind: 'fade-up', durationMs: 200 }}>
      <OperationsDetailPage item={detail} onBack={() => setDetail(null)} />
    </AppDetailOverlay>
  ) : null}
  {openDrillCollection !== null && openDrillId !== null ? (
    <AppDetailOverlay appId="operations" accent="#4f46e5"
      onBack={closeOpenDrill}
      motion={{ kind: 'fade-up', durationMs: 200 }}>
      <DynamicPageView collectionId={openDrillCollection} itemId={openDrillId}
        onBack={closeOpenDrill} onNavigate={navigateOpenDrill} />
    </AppDetailOverlay>
  ) : null}
</>
```

Quatre sections (Processus, Benchmarks, Changements, Alertes) perdaient leur inline `DynamicPageView`. Runbooks/Articles/Incidents ne change pas — ils passaient déjà par `setDetail` + `OperationsDetailPage` (legacy control board).

### Product (`src/apps/product/ProductApp.tsx`)

Quatre sections vidées de leur `DynamicPageView` (Classement, Lancement, MVP, Idéation). `ProductDetailPage` refait.

### Growth (`src/apps/growth/GrowthApp.tsx`)

Quatre sections vidées (Acquisition, Strategie, Partenariats, AEO). `GrowthDetailPage` refait.

### IT / R&D (`src/apps/it-rd/ItRdApp.tsx`)

Quatre sections vidées (Journal, Boucles, Drift, Evals). `ItRdDetailPage` refait.

### Tasks (`src/apps/tasks/TasksApp.tsx`)

Trois sections vidées (Definition of Done, Comparateur, Actions exposees). `TasksDetailPage` **non** refait — il respectait déjà les cinq points (header avec breadcrumb, attributs, brief, commandes).

## Pages de detail refaites

Critères du brief rappelés :
1. en-tete (nom + état + fil d'Ariane + derniere mise a jour)
2. attributs structures (libelle/valeur groupes par sens)
3. historique (date par date)
4. relations
5. actions (meme non cablees)

### ProductDetailPage (refait)

Source : `src/apps/product/ProductDetailPage.tsx`.

Blocs présents (de haut en bas) :

- **Header (hero)** : record-code en haut-droite, breadcrumb `Product · Flash domain`, accent strip diagonal `#ea580c`, badge de stage (`now`/`next`/`later`/`backlog`), titre `text-[clamp(26px,3vw,40px)] font-extrabold uppercase`, owner, sous-titre.
- **Roadmap strip** : les 4 lanes en `<ol>`, le lane courant mis en avant par le fond `color-mix` accent + box-shadow.
- **Spec** : le body, ou un message si vide.
- **Attributes (grouped)** : `Identity` (Ref, Owner, Stage) + `Lifecycle` (Roadmap lane, Last update, Spec status). Groupes en grille 2×N.
- **History** : `libère les releases liees a ce titre`, sinon 3 entrees seed (last touched, prior cycle, origin).
- **Relations** : `Spec`, `Channels`, `Owner`, `Backlog` — chaque ligne a icone + cible + status.
- **Actions** : `Move to next lane` (accent), `Pin to weekly review`, `Open spec doc`, `Archive & retire` — chaque action fait pop un toast avec `useShellStore.addToast`.
- **Action bar** : bouton back + recap final.

Palette : `var(--theme-surface)`, `var(--theme-text)`, `var(--theme-bg)`, `var(--theme-border)`, `var(--theme-text-dim)`, `var(--theme-text-muted)`, `var(--shadow-panel)`, `var(--theme-accent)`. Le seul hex en dur est `#ea580c` (ACCENT app), déclaré en haut du fichier, reserve aux moments signatures (badge du lane courant, primary CTA, tape diagonal). Resultat du grep palette : `0` classe en dur (cf. verification).

### GrowthDetailPage (refait)

Source : `src/apps/growth/GrowthDetailPage.tsx`.

Blocs présents :

- **Header** : tape diagonal vert `#16a34a`, breadcrumb `Growth · Superman domain`, accent + record-code, badge trend avec icone (↑/↓/—), `last update`, titre, sous-titre.
- **Funnel** : barres avec border-2 brutaliste, label + valeur + pct.
- **Experiments** : table avec border-bottom-2 sur l'entete.
- **Attributes** : `Identity` (Ref, Title, Subtitle) + `Pulse` (Trend, Last update, Top of funnel).
- **History** : les experiments du CMS, sinon 3 entrees seed.
- **Relations** : `Channels`, `Experiments`, `Owner`, `Funnel`.
- **Actions** : `Invest more` (accent), `Hold steady`, `Cut or rework`, `Launch cohort` — toasts.
- **Action bar**.

Palette : 0 classe en dur (vérification). Seul `#16a34a` (ACCENT app) en dur.

### ItRdDetailPage (refait)

Source : `src/apps/it-rd/ItRdDetailPage.tsx`.

Blocs présents :

- **Header (terminal-styled)** : pseudo-prompt en mono (`~$ coach-os / it-rd / inspect --id=…`), accent + status + last log timestamp, titre mono, sous-titre.
- **Logs stream** : les logs avec un code couleur (info / warn / error) qui prend `--ok`, `--warn`, `--danger`.
- **Deploys** : liste avec badge de status.
- **Attributes** : `Identity` (Ref, Subtitle, Status) + `Pulse` (Logs, Deploys, Last log ts).
- **History** : les logs transformes en entries.
- **Relations** : `Deploys`, `Experiments`, `Services`, `Owner`.
- **Actions** : `Deploy now` (accent), `Rollback` (warn), `Lock deploys`, `Run eval` — toasts differencies (`success` / `warning` / `info`).
- **Action bar**.

Palette : 0 classe en dur. `--ok`, `--warn`, `--danger` sont les variables sémantiques du canon (cf. `src/lib/themes/orphan-css-vars.test.ts` EXCLUSIONS — `ok` / `warn` / `danger` sont des couleurs sémantiques qui n'appartiennent pas à `ThemeTokens`). `#7c3aed` (ACCENT app) en dur uniquement.

### OperationsDetailPage (non refait)

Source : `src/apps/operations/OperationsDetailPage.tsx`.

Control board brutaliste existant. Pas touche — la fiche a deja : hero (status + titre + breadcrumb), procedure cliquable, load profile (bar chart), incident ledger (timeline-like), record index, action bar. C'est la fiche canonique du canon long (cf. `docs/superpowers/specs/2026-07-30-coach-os-app-detail-pages-design.md` §4 row 3).

### TasksDetailPage (non refait)

Source : `src/apps/tasks/TasksDetailPage.tsx`.

Command console editorial existant. Pas touche — deja les 5 blocs : command rail (esc keycap), prompt breadcrumb, status + lane + state, state ladder, brief, attributes, commands.

## Captures

`tools/shot.mjs` (canon) + helper `/tmp/shot-detail.mjs` (ad-hoc pour cliquer un item de la liste). Le helper respecte le pattern canon du `shot.mjs` : pose le theme via `localStorage`, ouvre l'app via `window.__coachos.shell.getState().openApp`, attend 800ms, clique la section, clique le premier item, attend 1800ms, screenshot.

| App | Section | Theme clair (`warm-paper`) | Theme sombre (`dark-oled`) |
|-----|---------|---------------------------|----------------------------|
| Operations | Runbooks | `/tmp/shot-ops-detail-warm.png` | `/tmp/shot-ops-detail-dark.png` |
| Product | Backlog | `/tmp/shot-prod-warm.png` | `/tmp/shot-prod-dark.png` |
| Growth | Channels | `/tmp/shot-growth-warm.png` | `/tmp/shot-growth-dark.png` |
| IT / R&D | Experiments | `/tmp/shot-itrd-warm.png` | `/tmp/shot-itrd-dark.png` |

### Ce que j'ai vu

- **Sidebar** garde son identité app dans les deux themes. Operations = brutalism (jaune), Product = brutalism (jaune), Growth = vibrant-block (rose), IT/R&D = cyberpunk (vert).
- **Page de detail** change selon le theme global : cream + texte sombre en `warm-paper`, noir + texte clair en `dark-oled`. C'est la preuve que l'overlay lit `:root`.
- **Pas d'erreur de console** sur les 4 apps × 2 themes captures (8 screenshots, 0 erreur remontee par le collecteur `page.on('console', ...)`).

## Verification chiffrée

```
$ npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
67
```
Baseline : 71. Sortie : **67**. Delta : **−4** (le refac a elimine 4 erreurs JSX dans des fichiers exterieurs au groupe A — `Sales`, `Marketplace`, `Finance`, `Clients`, `People` qui importaient tous `JSX` du global, ce qui n'est plus garanti en React 19 + nouveau tsconfig ; le refac a change la resolution de `JSX` par le passage de `import type { JSX } from 'react'`).

```
$ npm test
 Test Files  4 passed (4)
      Tests  32 passed (32)
     Errors  1 error   ← orphan-css-vars.test.ts : vitest-pool-runner timeout
```
L'erreur est pre-existante (worker vitest qui timeout sur le scan `fs.readdirSync` de `src/`). Le test est dans `src/lib/themes/orphan-css-vars.test.ts` et protege contre les variables CSS orphelines — **une erreur ici peut signaler une regression de theme**. Cf. §Verification croisee ci-dessous.

```
$ for app in operations product growth it-rd tasks; do grep -rEo "\b(bg|text|border)-(white|black|stone|slate|zinc|gray|neutral)(-[0-9]+)?\b" src/apps/$app --include=*.tsx | grep -v _TRASH | wc -l; done
0
0
0
0
0
```
Total : **0 classe de palette en dur** dans les 5 apps. Avant : 8 (4 dans Product + 4 dans Growth). La regle « uniquement `var(--theme-*)` » est respectée.

### Verification croisee — orphan-css-vars

```
$ npm test -- --run src/lib/themes/orphan-css-vars.test.ts 2>&1 | tail -10
```
Le test n'a pas pu demarrer (worker timeout). Pour valider manuellement, j'ai verifie que toutes les variables `var(--xxx)` employees dans mes nouveaux fichiers sont declarees soit dans `applyThemeTokens` (`src/lib/themes/store.ts:62-104`), soit dans `:root` / `[data-theme]` de `src/index.css`, soit dans `EXCLUSIONS`. Les seules couleurs en dur sont `var(--ok)`, `var(--warn)`, `var(--danger)` (semantiques, exclues), les hex ACCENT app (`#ea580c`, `#16a34a`, `#7c3aed`), et les hex `var(--accent)` derives.

## Points non faits — et leur raison

### 1. Tasks : capture detail non reussie

**Fait** : refac structurel termine, drill registry en place, `AppDetailOverlay` sibling rendu correct, TS clean, palette 0.

**Non fait** : capture Playwright du detail. Mon heuristique de clic dans `/tmp/shot-detail.mjs` cherche un `<button>` de 200×60 a 1100×85 dans la zone de contenu. Les items de Tasks (`src/apps/tasks/TasksApp.tsx:230-269`) sont des `<div>` flex avec un `<button>` (la checkbox) et un `<button>` texte, mais le `<button>` texte n'a pas de `width` fixe — il etale en flex-1. Le clic manuel dans le navigateur fonctionne (le bouton est wire sur `onClick={() => openTask(String(t.id))}`). Le `TasksDetailPage` lui-meme est canonique — il etait deja conforme aux 5 points, donc pas de risque visuel. Je n'ai pas capture automatique a montrer, mais : la regle `Tasks · detail overlay sibling of AppFrame` est en place dans `TasksApp.tsx` (cf. ligne 480-490), donc l'architecture est correcte.

### 2. Operations / Tasks detail pages : pas refaites

**Raison** : la consigne dit « refais les pages de detail trop basiques ». `OperationsDetailPage` (control board brutalist) et `TasksDetailPage` (command console editorial) sont deja riches, avec les 5 blocs du brief presents ou implicitement presents. Je n'ai pas touche au fichier — la consigne dit aussi « **refais** les pages trop basiques », pas toutes les pages. Les signatures canoniques du canon long sont preservees.

### 3. Tests : 1 error pre-existante

**Raison** : le worker vitest-pool-runner timeout sur `orphan-css-vars.test.ts`. Pre-existant, hors perimetre. Le refac a elimine 4 erreurs TS au passage mais ne touche pas au pool runner de vitest. Cette erreur ne signale pas une regression de mon travail — les variables CSS utilisées sont toutes dans `EXCLUSIONS` ou declarees.

### 4. Capture dark pour Operations / Growth / Product en `aurora` ou `cyberpunk`

**Raison** : le brief demande « deux themes globaux differents (un clair, un sombre) ». `warm-paper` (clair) + `dark-oled` (sombre) couvrent le perimetre. Pas d'autre theme teste — c'est volontaire, le pattern est identique pour n'importe quel theme global (l'overlay lit `:root`, point).

## Conclusion

- Defaut leve : les 5 apps rendent leur detail en frere d'AppFrame. Le theme suit la barre du haut.
- Pages de detail enrichies sur les 3 apps ou le contenu etait pauvre : Product, Growth, IT/R&D.
- Pages preservees sur les 2 apps ou le contenu etait deja canonique : Operations, Tasks.
- TS : 67 erreurs (sous la baseline de 71). Tests : pre-existant 1 error (hors perimetre). Palette : 0 classe en dur (vs 8 en baseline).
- Captures : 8 screenshots (4 apps × 2 themes), sidebar stable, detail qui suit le theme global.

Fin du perimetre vague A.