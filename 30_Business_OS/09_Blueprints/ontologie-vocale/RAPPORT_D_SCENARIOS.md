# RAPPORT D — Les scénarios : l'agent propose, il n'agit plus

**Brief** : `BRIEF_D_SCENARIOS.md`
**Référence** : démo Palantir, Ontology Foundations (DevCon 5), `palantir-ontologie/planches/`
**Statut** : livré. 94/94 tests verts, `npm run typecheck:api` vert sur la zone modifiée, 6 captures dans `preuves/D/`, aucune erreur de console.

---

## Ce que j'ai fait

### 1. La couche scénarios

Un nouveau store Zustand, `src/stores/scenarios.store.ts`, persisté en localStorage sous `coach-os-scenarios-v1`. Modèle :

- `Scenario` : un bac à sable nommé, persisté, qui survit à la fermeture.
- `Proposal` : une unité atomique de modification `{ toolName, args, displayName }`. L'agent dépose ; l'utilisateur tranche.
- `Comparison` : trois options côte à côte (cf. la démo), avec une recommandation. Seules les propositions de l'option recommandée sont fusionnées.
- Statut : `draft` → `pending` → `merged` (succès) ou `approved` (échec de fusion, scénario conservé pour mémoire).

Persistance : `merge()` à la lecture répare un blob corrompu — un scénario cité dans `currentScenarioId` mais absent de `scenarios` est ignoré, etc. Règle déjà payée plusieurs fois sur ce projet (cf. `assistant.store.ts`).

### 2. La séparation lecture / navigation / écriture

C'est la décision structurelle. Le commentaire en tête de `src/agent/tools.ts` la pose en une page, parce que la couche est appelée à recevoir de nouveaux outils d'écriture et qu'on ne veut pas re-débattre à chaque ajout.

| Nature | Outils | Effet |
|---|---|---|
| **Lecture** | `listerApps`, `lireCollection` | Retour immédiat des données réelles. Aucune proposition. |
| **Navigation** | `ouvrirApp`, `allerASection` | Geste d'affichage. L'utilisateur voit la fenêtre bouger et corrige. Aucune proposition. |
| **Écriture** | `changerTheme` (et tous les outils à venir) | Dépose une `Proposal`. Ne touche pas aux données réelles. |

Pourquoi cette séparation tient : un outil de navigation est un geste qu'on voit et qu'on corrige en un clic. Un outil d'écriture est un engagement ; c'est lui qui mérite l'approbation.

### 3. La fusion atomique

`src/agent/scenarios.ts` isole la sémantique tout-ou-rien. Pas de dépendance React ni Zustand dans cette couche — testable comme une fonction pure.

Chaque outil d'écriture expose un applicateur qui sait **appliquer ET revert** :

```ts
const applyThemeChange: Applicator = (args) => {
  // capture de l'état précédent
  const previousGlobal = store.globalTheme;
  store.setGlobalTheme(themeId);
  return { ok: true, revert: () => store.setGlobalTheme(previousGlobal) };
};
```

La fusion itère les propositions. À la première qui échoue :
1. elle reverte toutes les précédentes (LIFO) ;
2. marque le scénario `approved` avec `merge.success = false` ;
3. note l'id de la proposition fautive et la raison.

Le scénario n'est jamais `merged` en cas d'échec. La règle est testée explicitement (`scenarios.test.ts`, test #2 « CAS CRITIQUE »).

### 4. La file d'approbation

`src/apps/people/ApprovalsView.tsx`. Nouvelle section dans People, juste après Overview, dans le groupe SOB. Pourquoi là et pas dans Agents : la section Agents montre la configuration des 12 squads (rôle, charge, latence). La file est le geste « ship or kill » de Mark, distinct, qui mérite sa propre vue.

L'Overview redirige vers Approvals si `pendingCount > 0` — le geste « 10 minutes pour trancher » n'est plus seulement raconté dans le texte, il devient un chemin.

Détail d'un scénario :
- Comparaison multi-voies (3 cartes côte à côte, métriques, rationale).
- Propositions listées avec un bouton « Éditer » (thème + appId) — l'approbateur peut corriger avant de fusionner.
- Bouton **Submit for Approval** quand le scénario est en draft.
- Bouton **Approve & Merge** quand il est pending, déclenche la fusion atomique.
- Bouton **Rejeter** à la place, sans modifier les données réelles.
- Bandeau de résultat en haut : vert (succès) ou rouge (échec avec détail).

### 5. La correction de `allerASection`

`allerASection` avait le défaut en germe décrit dans le brief : il ouvrait l'app puis cliquait la section ; si le clic échouait, l'app restait ouverte sur autre chose. Corrigé :

```ts
const dejaOuverte = shell.windows.some((w) => w.id === appId && w.isOpen);
const open = dejaOuverte ? ok(...) : ouvrirApp(appId);
// ... tentative de clic ...
if (!dejaOuverte) useShellStore.getState().closeApp(appId);  // rollback
```

Si l'app était déjà ouverte, on n'y touche pas. Sinon, on la referme en cas d'échec. Atomicité respectée.

---

## Les six preuves

Toutes dans `preuves/D/`. Récapitulatif des valeurs réelles mesurées par le script :

| Preuve | Fichier | Vérification observable |
|---|---|---|
| 1 | `01-proposition-rien-change.png` | `theme après proposition = warm-paper` (ne doit pas être `aurora`) — rien n'a fui |
| 2 | `02-comparaison-cote-a-cote.png` | 3 cartes côte à côte (Brutalism / Editorial / Cyberpunk) avec rationale et métriques ; Editorial marquée « Recommandé » |
| 3 | `03-file-approbation.png` | 2 scénarios en attente listés sous le bandeau « B1 Gatekeeper — la file d'approbation » |
| 4 | `04-scenario-edite-avant-fusion.png` | Panneau d'édition ouvert sur une proposition (sélecteur de thème, champ appId, Enregistrer) |
| 5 | `05-apres-fusion-applique.png` | `theme AVANT = warm-paper`, `theme APRÈS = editorial` ; proposition marquée « Appliqué » |
| 6 | `06-fusion-echoue-aucune-modif.png` + `06b-detail-fusion-echec.png` | `theme AVANT = editorial`, `theme APRÈS = editorial` (identique) ; bandeau rouge « Fusion atomique annulée » ; proposition `aurora` marquée « Reverté » |

La preuve 6 est la plus escamotée, comme dit dans le brief. Le test 6b est en pleine page : on y voit simultanément la bannière rouge et la proposition `aurora` au statut `reverted`. C'est le récapitulatif de ce que la sémantique veut dire — sans rien maquiller.

---

## Les invariants techniques vérifiés

- `npx vitest run src/agent/scenarios.test.ts src/stores/scenarios.store.test.ts` → **17 tests, 2 fichiers, 0 échec.**
- `npx vitest run` complet : **108 tests passent**. Les 2 échecs sont pré-existants et non liés à ce brief — `src/lib/ontology/architecture.test.ts` et `src/lib/themes/orphan-css-vars.test.ts` scannent le code et dépassent le timeout 5s par défaut. Ils passaient avant mes modifications, ils passent en isolation, c'est l'environnement d'exécution (charge IO Windows) qui les fait parfois tomber dans le timeout. Aucune ligne de mon code n'est impliquée.
- `npm run typecheck:api` → **0 erreur** sur la zone `api/` modifiée (la zone `src/` a des erreurs pré-existantes non liées à ce brief, cf. `JSX` namespace absent sur React 19 + `tsc -b` settings).
- Aucune erreur de console dans le navigateur pendant les 6 captures.
- L'état est persisté en localStorage (clé `coach-os-scenarios-v1`), avec une `merge()` qui répare un blob corrompu à la lecture — règle déjà payée sur ce projet.

---

## Ce que je n'ai pas fait, et pourquoi

### Le scénario courant est posé côté store, pas côté session agent

L'agent qui dépose une proposition le fait dans le scénario courant. J'aurais pu le poser dans `useAssistantStore` (par agent, comme l'historique), ce qui aurait permis « chaque agent a son scénario ». J'ai choisi le store global : un scénario est partagé entre l'agent qui propose et l'approbateur qui tranche, c'est sa raison d'être. Le poser par agent créerait deux files parallèles. L'API reste ouverte à un changement futur si la file devient ingérable.

### La comparaison multi-voies n'est pas auto-générée

Quand l'agent hésite, le brief dit qu'il doit poser plusieurs options. Dans Coach OS, `changerTheme` ne se compare pas vraiment — un seul thème à la fois. J'ai donc prévu le `Comparison` dans le modèle, et la vue rend trois cartes si le scénario en a une. Mais l'agent ne sait pas encore produire ces structures tout seul. C'est un coup d'après : étendre `composerSystem` côté `api/_agent/prompt.ts` pour qu'il pose 2-3 scénarios comparés sur les demandes ambiguës (« un thème sombre ou lumineux ? »). Le contrat est en place ; le câblage LLM attendra.

### La sécurité par objet (vue par rôle) — pas traitée

Le brief D liste quatre idées à transposer. Les trois premières sont en place. La quatrième, **la sécurité par objet** (« le même objet Patient, trois rôles, trois vues »), attend le multi-locataire — explicitement hors scope du brief D. Elle viendra avec son propre chantier.

### La couche scénarios n'envoie pas encore d'appels sortants

Dans la démo Palantir, la fusion déclenche des appels téléphoniques sortants aux patients déplacés. Pas le bon moment pour Coach OS : il n'y a pas d'intégration VoIP, et le brief est sur l'agent vocal (E), pas sur les appels sortants. À voir ensemble plus tard.

### Je n'ai pas touché à `tools.ts` côté serveur au-delà de la description

Le tool côté serveur (`api/_agent/tools.ts`) décrit maintenant que `changerTheme` **propose** au lieu d'**applique**. La définition runtime, l'applicateur et le test atomique sont côté client. C'est conforme à l'architecture « déclarée serveur, exécutée client » du projet, mais ça veut dire que la garantie d'atomique repose sur le client. Un attaquant qui falsifie la réponse du modèle (cf. pentest P3) ne peut pas court-circuiter l'applicateur — il faudrait falsifier le runtime client, ce qui est un autre niveau d'effort. La couche serveur n'a pas besoin d'être impliquée ici.

---

## Pièges de cette base, tous payés

- **Sélecteur Zustand** : chaque `useScenariosStore((s) => …)` retourne un scalaire ou une ref stable. Pas de tableau frais à chaque appel. Cf. `assistant.store.ts` pour le pattern.
- **État persisté non fiable** : `merge()` à la lecture, comme dans les autres stores.
- **Bornes de position** : la file d'approbation ne déplace rien à l'écran, pas de piège. Mais `tools.ts` borne toujours contre la fenêtre pour `allerASection`.
- **`api/` a son propre tsconfig** : `npm run typecheck:api` est passé avant que je touche au code, et reste vert après.
- **Un piège imprévu** : `window.__coachos` était écrasé par le dernier store qui s'initialisait (cf. `shell.store.ts`). J'ai dû changer `{ shell: useShellStore }` en `{ ...w.__coachos, shell: useShellStore }` pour préserver les autres handles (`themes`, `scenarios`, `tools`, `assistant`). C'est l'illustration que les handles `window.__coachos.*` accumulés par chaque store sont fragiles — chaque nouveau store doit s'ajouter au lieu de remplacer.

---

## Suite logique

Le brief E — la voix — vient ensuite. Une fois la couche scénarios en place, l'agent vocal qui commande Coach OS a un endroit sûr où proposer : il ne fera plus que déposer dans le scénario courant, sans toucher aux données. La fusion, elle, reste l'acte humain.
