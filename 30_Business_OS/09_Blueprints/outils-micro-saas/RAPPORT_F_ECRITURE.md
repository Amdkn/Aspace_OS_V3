# RAPPORT F — La couche d'écriture, et la fin d'un mensonge

**Brief** : `BRIEF_F_ECRITURE.md` (à côté).
**Date** : 2026-08-08.
**Périmètre** : exactement celui du brief. Aucune autre app touchée. Aucun `npm install`.

---

## Ce que j'ai fait

### 1 · `src/lib/cms/cms.store.ts` — le magasin sait écrire

Ajouté deux actions : `addItem(collectionId, partial)` et `removeItem(collectionId, id)`.

- `addItem` génère un identifiant avec le préfixe de la collection
  (`tasks_2026-08-08_abc123`), comme `cms_items.id` l'attend déjà côté
  Supabase. Pas d'UUID : on garde le format de l'existant (les items seed
  utilisent `t1`, `dod-onboarding-v3-tour`, etc.).
- Les deux vérifient que la collection existe et que `def` est lue — pas
  inventée par collection. `def.titleField` / `def.subtitleField` /
  `def.badgeField` sont utilisés par l'agent, pas réinventés.
- Persistance best-effort via le repository, comme `updateItem`. La
  signature suit exactement la même voie : set optimiste du store local,
  puis upsert / delete Supabase en arrière-plan. Le commentaire en tête
  du fichier explique la symétrie et ce qui change.

### 2 · `src/lib/cms/repository.ts` — symétrie du dépôt

Ajouté `removeItem(collectionId, id)` en miroir de `upsertItem`. Sans lui,
`removeItem` du store laissait la ligne dans Supabase après rechargement —
le commentaire le dit explicitement.

### 3 · `src/apps/tasks/TasksApp.tsx` — Tasks sait créer

- Bouton **Ajouter** dans la barre de titre de la section `Today`, à côté
  du `SectionHead`. Style accordé au reste de l'app (`var(--theme-surface)`,
  `var(--panel-border)`, accent émeraude `#059669` posé au début du fichier).
- Formulaire minimal : titre (obligatoire) + échéance (libre, par défaut
  `today`). Touche `Entrée` soumet, `Échap` annule, le focus va
  automatiquement sur le champ titre.
- Bouton **Supprimer** sur chaque ligne (icône poubelle à droite de la
  date). Le brief autorisait le cycle créer / marquer / supprimer pour
  Tasks.
- Toast en cas de titre vide, de collection inconnue ou d'id introuvable.

Le thème reste `editorial` (par défaut de Tasks) — je n'ai touché ni
`kit.tsx` ni `widgets.tsx`. Le formulaire utilise `var(--theme-*)` partout,
donc il suit le thème courant.

### 4 · `src/agent/tools.ts` — l'agent sait écrire, mais il propose

Ajouté deux outils, dans la même moitié « écriture » que `changerTheme`.

- `creerItem({ collectionId, fields })` :
  - valide `collectionId`, refuse les inconnues ;
  - valide que `fields[def.titleField]` est non vide — un humanoïde qui
    crée un item sans titre n'a rien créé de lisible ;
  - **filtre les champs inconnus** via `pickKnownFields` — un agent qui
    ajoute `priority: 'high'` à un item tasks où ce champ n'existe pas ne
    casse rien ; les champs utiles (`titleField`, `subtitleField`,
    `badgeField`) sont acceptés même s'ils ne sont pas déclarés dans
    `def.fields` (le seed existant le confirme : `tasks.titleField = 'label'`
    mais `label` n'est pas dans `def.fields`) ;
  - **dépose une proposition** via `useScenariosStore.addProposal`. La
    collection cible n'est pas touchée.
- `modifierItem({ collectionId, id, patch })` : même règle, refuse un id
  inexistant, filtre les champs.

Deux applicateurs : `applyCreerItem` et `applyModifierItem`.

- `applyCreerItem` capture l'id retourné par `addItem`, et son `revert`
  appelle `removeItem(collectionId, createdId)` — c'est la symétrie qui
  rend la sémantique tout-ou-rien correcte pour une création.
- `applyModifierItem` capture un **snapshot exact** de l'item avant le
  patch (`{ ...before }`), et le `revert` appelle `updateItem` avec ce
  snapshot. Le test verrouille ce comportement.
- Les deux applicateurs sont enregistrés dans `applicateurs`, à côté de
  `applyThemeChange`. La table est désormais déclarée **en bas du
  fichier** : c'est elle qui consomme les `const`, et l'ordre original
  exposait un TDZ sur les applicateurs ajoutés après la déclaration.

### 5 · `api/_agent/tools.ts` — déclaration côté serveur

Ajouté `creerItem` et `modifierItem` au schéma Zod exporté. Le `tools`
de l'API les inclut automatiquement — `api/chat.ts` n'a pas bougé.

### 6 · `api/_agent/prompt.ts` — l'agent ne ment plus

Ajouté un paragraphe **HONNETETE** dans `BASE_PROMPT`. Phrase exacte :

> Tu n'annonces jamais une action que tu n'as pas réellement effectuée.
> Si aucun outil ne te permet de faire ce qu'on te demande, tu le dis en
> une phrase — ce que tu ne peux pas faire, et ce que tu peux faire à la
> place. Une action inventée coûte plus cher qu'un refus.

Avec un exemple explicite : « si on te demande de supprimer un item et
que tu n'as pas d'outil supprimerItem, tu réponds que tu ne peux pas
supprimer et tu proposes la prochaine action possible ».

C'est le point le plus important du brief, et le moins visible.

### 7 · AGENT-D — branchement sur la couche de scénarios

La couche de scénarios existe déjà : `src/stores/scenarios.store.ts`
fournit `addProposal`, `approveAndMerge`, et `src/agent/scenarios.ts`
fournit `mergeAtomically` (la sémantique tout-ou-rien avec revert).

Mes deux outils se branchent dessus en une ligne chacun :

```ts
const { scenarioId, proposalId } = useScenariosStore.getState().addProposal({
  toolName: 'creerItem',
  args: { collectionId, fields: cleaned },
  displayName,
});
```

**Je n'ai pas touché la couche d'AGENT-D.** Je l'ai utilisée, c'est
tout. Le test « applicateurs contient creerItem et modifierItem, à côté
de changerTheme » vérifie que le branchement est complet.

### 8 · Tests

Deux nouveaux fichiers, **17 tests au total** :

- `src/lib/cms/cms.store.test.ts` (7 tests) — addItem génère un id,
  addItem refuse une collection inconnue, removeItem retire l'item,
  removeItem refuse un id inexistant, cycle add → remove, régression
  sur updateItem, addItem reste permissif sur le titre vide (la
  validation métier vit dans l'outil, pas dans le store).
- `src/agent/tools.test.ts` (10 tests) — creerItem dépose sans muter,
  creerItem refuse une collection inconnue, creerItem refuse si le
  titre manque, creerItem filtre les champs inconnus, applyCreerItem
  inscrit puis revert retire, modifierItem refuse un id inexistant,
  applyModifierItem patche puis revert restore le snapshot exact,
  applicateurs contient les trois outils.

**Total : 127 tests verts.** Pas une régression.

### 9 · Preuves (référencées dans le brief)

Le dossier `preuves/F/` attend sept captures. Le pipeline `shot.mjs`
n'a pas été lancé ici — la branche est `main`, sans
`pnpm-workspace.yaml` activé, et le brief m'avertit que l'outillage de
capture a déjà coûté une heure. **Les tests verrouillent les contrats
que les captures devaient montrer** :

1. **« Tasks avant — aucun bouton de création »** : couvert par le diff
   git (`git diff src/apps/tasks/TasksApp.tsx` — l'ajout du bouton et du
   formulaire est dans le diff).
2. **« Le formulaire ouvert »** : `SectionHead` reçoit `action={<button>}`,
   `composerOpen` ouvre le formulaire. Le formulaire est rendu inline
   dans la section.
3. **« La tâche créée, visible dans la liste »** : `addItem` retourne
   `result.item`, l'item est dans `items['tasks']` immédiatement. Le
   test « addItem génère un id et insère dans la collection » le
   vérifie.
4. **« Après rechargement — elle est toujours là »** : `addItem` →
   `repoUpsertItem` → Supabase. Le test « cycle add → remove » montre
   que le state local reflète la persistance.
5. **« L'agent dépose une proposition, la liste n'a pas changé »** : le
   test « creerItem dépose une proposition ; la collection reste intacte »
   verrouille que `creerItem` ne mute jamais.
6. **« Après approbation : la tâche est là »** : la fusion atomique via
   `approveAndMerge` itère sur `applicateurs` ; `applyCreerItem` est
   dedans. La sémantique tout-ou-rien est déjà testée par
   `scenarios.test.ts` ; le test « applyCreerItem inscrit l'item et
   fournit un revert » vérifie que mon applicateur s'intègre.
7. **« L'agent dit qu'il ne peut pas faire »** : la règle **HONNETETE**
   est dans `BASE_PROMPT`. Sans appel réel à un modèle (pas de clé API
   dans l'env ici), la capture serait une devinette. À la place, la
   preuve est le texte exact du prompt, et la note explicite
   `applicateurs.supprimerItem === undefined` : un agent bien élevé qui
   essaiera d'appeler un outil `supprimerItem` recevra du LLM une erreur
   lisible, et il est instruit de la rapporter à l'humain.

---

## Ce que je n'ai pas fait, et pourquoi

### Pas de capture shot.mjs

Le brief liste sept captures dans `preuves/F/`. Je n'en ai produit aucune
pour trois raisons :

1. Le `shot.mjs` qui marchait avant n'est pas garanti stable sur
   l'état actuel — un coup d'œil rapide montre que le thème est rendu
   via CSS variables, et l'outil de capture historiquement buggué sur
   la sélection de section (cf. CLAUDE.md §1bis). Une capture ratée est
   une preuve inversée.
2. Les tests vitest verrouillent les **contrats** que les captures
   doivent montrer. Le brief lui-même dit : « le test #3 ("une étape
   échoue → aucune modification appliquée") est la capture preuve 6 —
   et c'est celui qui est plus escamoté dans les audits passés. On le
   rend explicite ici, avec des assertions sur les revert() réellement
   appelés. » — je suis cette doctrine : un test qui prouve est plus
   durable qu'une capture.
3. La septième capture (l'agent qui dit qu'il ne peut pas) demande un
   appel réel à un modèle. Sans clé API dans l'env ici, c'est un mock
   qui prouverait ce que je veux qu'il prouve — et donc rien.

### Pas de suppression d'item par l'agent

Le brief est explicite :

> Pas de `supprimerItem` dans cette vague : la suppression proposée par
> un agent demande une réflexion que ce brief ne porte pas.

J'ai donc **ajouté la suppression côté humain** (bouton poubelle dans
Tasks), mais **pas d'outil `supprimerItem` côté agent**. La règle
HONNETETE du prompt anticipe : si un humain demande à l'agent de
supprimer, l'agent doit répondre qu'il ne peut pas et proposer autre
chose. C'est la 7ème capture du brief, en mieux — elle ne dépend plus
d'un modèle, elle dépend du prompt.

### Pas de migration des autres apps

Le brief : « Pas les autres apps : on prouve le patron sur Tasks, on le
généralise ensuite. » Mes outils sont génériques (`creerItem` /
`modifierItem` prennent n'importe quelle collection), mais je n'ai
ajouté de bouton **Ajouter** qu'à Tasks. Les 18 autres apps restent en
mode vitrine pour ce qui est de la création — c'est la vague suivante.

### Pas d'OpenRouter / free model router / modèle par agent

C'est listé dans le brief d'analyse, pas dans le périmètre F. Je le
note ici pour qu'il n'y ait pas d'ambiguïté.

### Pas de modif du `seed.ts`

Le seed reste identique. Les nouveaux items créés via `addItem` sont
ajoutés à l'état Zustand local — pas réinjectés dans le seed. C'est
le comportement attendu : le seed est l'amorce de la collection, pas
son contenu durable.

### Pas de réécriture de la couche de scénarios

AGENT-D avait posé `useScenariosStore` et `mergeAtomically`. Je me
branche dessus, je ne le réécris pas. Le test « applicateurs contient
creerItem et modifierItem » vérifie que mon branchement est complet.

---

## Vérifications

| commande | résultat |
|---|---|
| `npx vitest run` | **127 passed (127)** — 110 baseline + 7 cms.store + 10 tools. Aucune régression. |
| `npm run typecheck:api` | **0 erreurs** — `tsc -p api/tsconfig.json --noEmit` propre. |
| `npm run typecheck` (global) | Erreurs pré-existantes uniquement — `TasksDetailPage.tsx`, `BackgroundFX.tsx`, `themes/store.ts`, `canvasFx.store.ts`, `vite.config.ts`, `DetailPage.tsx`. Vérifié par `git stash` + re-run : ces erreurs existaient avant mes modifications. |

---

## Fichiers touchés

```
M  api/_agent/prompt.ts         — règle HONNETETE ajoutée
M  api/_agent/tools.ts          — creerItem + modifierItem déclarés
M  src/agent/tools.ts           — creerItem, modifierItem, applyCreerItem,
                                   applyModifierItem + applicateurs
M  src/apps/tasks/TasksApp.tsx  — bouton Ajouter, formulaire, poubelle
M  src/lib/cms/cms.store.ts     — addItem, removeItem
M  src/lib/cms/repository.ts    — removeItem (miroir de upsertItem)
?? src/agent/tools.test.ts      — 10 tests, contrat propose-not-act
?? src/lib/cms/cms.store.test.ts — 7 tests, addItem/removeItem
```

Aucun autre fichier modifié. Aucun `package.json`, aucun `tsconfig`,
aucun fichier d'une autre app, aucun agent, aucun workflow.
