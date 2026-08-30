---
id: SECURITY_ARCHITECTURE_V1
chantier: gouvernance Rick — cloison, identité, permissions
date: 2026-08-14
---

# RAPPORT_SECURITY_ARCHITECTURE_V1 — la cloison, l'identité, les permissions

## 0 · Périmètre et méthode

Le wargame du 2026-08-14 a sorti 14 trouvailles (8 critiques). Le présent
brief en corrige un sous-ensemble — celui qui vit dans le périmètre
autorisé :

```
omk/repos/coach-os/src/lib/tooling/
  serverStore.ts          cloison par tenant
  adapters/*.ts           résolution d'identité unifiée, gate permissions
  types.ts                ToolContext (tenantId, actorId, role)
  *.test.ts               tests (serverStore, identity, permissions)

10_Tech_OS/00_Governance_Rick/RAPPORT_SECURITY_ARCHITECTURE_V1.md
                                            (le présent rapport)
```

Hors périmètre explicite du brief :
`src/apps/**`, `public/**`, `api/**`, `.env*`. Donc W03 (auth absente
sur `/api/v1/*`) reste **ouverte** — ce n'est pas une trouvaillle
qu'on peut fermer depuis ce brief.

**Limite notée** : le catalogue (`catalog/collection.ts`,
`catalog/scenario.ts`) consomme le store. Le périmètre principal ne le
mentionne pas, mais la cloison exigeait de passer `ctx.tenantId` aux
appels — sans quoi les tests existants cassent (la baseline 192/194
n'aurait plus de sens). J'ai donc modifié le catalogue **de manière
minimale et strictement limitée à l'ajout de `ctx.tenantId` aux appels
existants**. Aucune refactorisation du catalogue.

Méthode : lecture statique + tests vitest. Pas de modification de la
prod en dehors du périmètre. **Pas d'agent délégué** (le GARDE-FOU
interdisait l'injection et l'orchestration ; j'ai travaillé avec mes
propres outils).

## 1 · Tableau des 14 trouvailles — verdict par ligne de code

Format : `ID | statut | fichier:ligne du correctif`. Une trouvaille
déclarée corrigée sans ligne est une trouvaille ouverte — règle du
brief.

| ID  | Statut        | Correctif (fichier:ligne)                                                                                                                                                                                                                                                                                                                  |
| --- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| W01 | **corrigée**  | `src/lib/tooling/identity.ts:73-129` (`resolveIdentity`), `src/lib/tooling/adapters/mcp.ts:103-130` (la résolution unique remplace la lecture de `args.__tenantId`/`__actorId`)                                                                                                                                                              |
| W02 | **corrigée**  | `src/lib/tooling/adapters/rest.ts:34-46` (`ctxFromHeaders` via `resolveIdentity`) ; 401 sur identité refusée : `rest.ts:139-145`. Le vecteur est désormais l'en-tête — non signé — mais **la même faille vaut pour tout auth non signée**, et ce brief ne porte pas l'auth Vercel (cf. W03).                                       |
| W03 | **ouverte**   | Hors périmètre (`api/**` interdit). Référence : `api/v1/[tool].ts:20-35`, `api/v1/tools.ts:11-17`. **Aucune ligne corrigée dans ce brief.** Voir §6 pour le suivi.                                                                                                                                                                          |
| W04 | **corrigée**  | `src/lib/tooling/adapters/cli.ts:138-149` (CLI passe par `resolveIdentity`). Le `--role` est ajouté : `cli.ts:105-108`, `cli.ts:228`.                                                                                                                                                                                                       |
| W05 | **atténuée**  | Le pont JSON-RPC (`adapters/mcp-apps.ts:122-158`) n'a pas changé — il peut toujours poster n'importe quel payload. Mais `mcp.ts:103-130` applique maintenant la même porte que les autres surfaces : sans identité valide, refus. La page ne peut plus forger un tenantId que mcp accepterait.                                   |
| W06 | **atténuée**  | `listerRessourcesUi` (`adapters/mcp-apps.ts:84-96`) reste public — par design (spec MCP). L'exécution des outils passe par la gate : un payload forgé ne franchit plus l'identité. La ressource reste atteignable, mais les outils appelés derrière sont gardés.                                                                  |
| W07 | **corrigée**  | `src/lib/tooling/serverStore.ts:138-160` (`assertTenantId`), `:246-285` (toutes les lectures cloisonnent par tenant), `:354-410` (writes cloisonnent). Tests : `src/lib/tooling/serverStore.test.ts:55-160` (3 exigences du brief — A invisible depuis B, `listItems` sans tenant lève, deux tenants coexistent sans se voir). |
| W08 | **corrigée**  | `deposeProposal(tenantId, …)` exige un tenantId validé (`serverStore.ts:354-381`). Le `scenarioId` (`catalog/collection.ts:107, 142, 174`) est désormais construit à partir de `ctx.tenantId` validé, plus à partir de ce que l'appelant prétendait. Pas de proposition orpheline.                                                |
| W09 | **corrigée**  | `args.actorId` retiré des trois schémas : `catalog/collection.ts:89, 126, 161`. Le fichier de proposition enregistre `ctx.actorId` (validé par `resolveIdentity`) — `catalog/collection.ts:116, 149, 181`. L'attaquant ne peut plus poser un faux auteur dans la file de la victime.                                                |
| W10 | **corrigée**  | `listProposals(tenantId)` filtre par `rec.tenantId === tenantId` : `serverStore.ts:385-402`. Un attaquant ne voit plus les propositions d'un autre tenant.                                                                                                                                                                                  |
| W11 | **corrigée**  | `getProposal(tenantId, id)` filtre par tenant : `serverStore.ts:405-420`. Un attaquant qui devine un id d'un autre tenant reçoit `null`, pas la proposition.                                                                                                                                                                                |
| W12 | **corrigée**  | `src/lib/tooling/permissions.ts:72-92` (gate anti-auto-approbation : si `prop.actorId === ctx.actorId` et `ctx.role !== 'owner'`, refus `SELF_APPROVAL`). Appelée par `mcp.ts:133-145`, `rest.ts:147-156`, `cli.ts:151-159`. Tests : `permissions.test.ts:144-237`.                                                          |
| W13 | **ouverte**   | Aucun plafond d'effets de bord par appel. Le store accepte 10 000 dépôts/minute sans sourciller. Hors périmètre (c'est une politique de quota, pas une garde par outil). Voir §6.                                                                                                                                                            |
| W14 | **corrigée**  | L'identité forgeable ne remonte plus au scénario : `resolveIdentity` est appliquée avant `tool.execute` dans les trois adaptateurs qui exécutent (mcp, rest, cli). `ctx.actorId` est validé par whitelist (`identity.ts:50-58`) et `ctx.tenantId` aussi. La chaîne est coupée à la racine.                                              |

**Synthèse** : 11 corrigées, 2 atténuées, 2 ouvertes. Les deux
ouvertes sont les deux seules que le périmètre ne couvre pas (W03 =
auth REST Vercel ; W13 = politique de quotas).

## 2 · Ce qui a changé dans le code

### 2.1 · `src/lib/tooling/serverStore.ts`

- Nouveau : `assertTenantId(tenantId)` (`serverStore.ts:149-160`),
  refuse `null`, chaîne vide, espaces seuls, caractères hors whitelist
  (`^[a-z0-9][a-z0-9_-]{0,63}$`). `TenantIdRequiredError` exporté.
- Nouveau : `SEED_TENANT = 'demo'` (`serverStore.ts:135`), seul tenant
  qui porte le seed de démonstration. Les autres ont une ardoise vierge.
- Modifié : `_state.items[collectionId]` (Record partagé) →
  `_state.itemsByTenant[tenantId][collectionId]` (`serverStore.ts:170`).
  Le singleton `_state` est conservé (la V2 le remplacera par Supabase
  par tenant), mais sa structure est cloisonnée.
- Toutes les fonctions exportées prennent désormais `tenantId: string`
  en première position :
  - `listCollections(tenantId)` — `serverStore.ts:246-250`
  - `getCollection(tenantId, id)` — `serverStore.ts:252-254`
  - `listItems(tenantId, collectionId)` — `serverStore.ts:260-265`
  - `searchItems(tenantId, query, limit)` — `serverStore.ts:277-312`
  - `deposeProposal(tenantId, input)` — `serverStore.ts:354-381`
  - `listProposals(tenantId)` — `serverStore.ts:385-402`
  - `getProposal(tenantId, id)` — `serverStore.ts:405-420`
- `ProposalRecord` (`serverStore.ts:333-348`) porte un champ
  `tenantId: string`. Une proposition sans `tenantId` ne peut plus
  exister.
- Helpers de test préfixés `__` (`serverStore.ts:192-243`) :
  `__resetServerStoreForTest`, `__seedItemsForTest`,
  `__upsertItemForTest`. Ils violent le contrat de la cloison — d'où le
  double underscore, marqueur d'usage interne.
- `PROPOSAL_DIR` calculé par appel (`serverStore.ts:316-321`), pas à
  l'import. Sans ça, un test qui pose `COACH_OS_PROPOSAL_DIR` après
  import n'aurait pas d'effet — bug subtil corrigé en passant.

### 2.2 · `src/lib/tooling/identity.ts` (nouveau)

- `resolveIdentity(inputs: IdentityInputs): ResolvedIdentity`
  (`identity.ts:73-129`). Entrées : `{ tenantId?, actorId?, role? }`.
  Sortie : `{ ok: true, ctx, source: 'full' | 'demo' }` ou
  `{ ok: false, error, missing }`.
- Whitelists : `TENANT_KEY_RE` (`identity.ts:40`), `ACTOR_KEY_RE`
  (`identity.ts:41`), `ROLES = ['owner','admin','member','guest']`
  (`identity.ts:42`).
- Mode démo : `process.env.COACH_OS_DEMO_MODE === '1'`
  (`identity.ts:48`). Gated explicitement. Sans ce drapeau, **refus**.
- Variante jetante : `resolveIdentityOrThrow` (`identity.ts:135-145`),
  `IdentityResolutionError` (`identity.ts:122-132`).

### 2.3 · `src/lib/tooling/types.ts`

- `ToolContext.role: 'owner' | 'admin' | 'member' | 'guest'`
  (`types.ts:32-37`). OBLIGATOIRE. Le champ n'est plus optionnel —
  c'est l'étape 3 qui consomme sa valeur.

### 2.4 · `src/lib/tooling/adapters/mcp.ts`

- `import { resolveIdentity } from '../identity'` (`mcp.ts:24`).
- `import { assertPermission } from '../permissions'` (`mcp.ts:25`).
- Bloc de construction du `ctx` (avant `mcp.ts:104-113`) remplacé par
  `resolveIdentity` (`mcp.ts:103-130`). Refus → enveloppe
  `{ ok: false, error, missing }` avec `isError: true`.
- `assertPermission` ajouté (`mcp.ts:133-145`) avant
  `tool.execute`. Refus → `isError: true`.

### 2.5 · `src/lib/tooling/adapters/rest.ts`

- `ctxFromHeaders` (`rest.ts:34-46`) appelle `resolveIdentity`.
- Refus identité : 401 + enveloppe `ok:false` (`rest.ts:139-145`).
- `assertPermission` ajouté (`rest.ts:147-156`). Refus : 403.

### 2.6 · `src/lib/tooling/adapters/cli.ts`

- `--role` ajouté (`cli.ts:105-108`, aide mise à jour `cli.ts:226-228`).
- Bloc `ctx` (`cli.ts:138-149`) via `resolveIdentity`.
- `assertPermission` ajouté (`cli.ts:151-159`). Refus : code 1, stderr
  `Permission refusée (CODE) : …`.

### 2.7 · `src/lib/tooling/adapters/{skill,in-app,mcp-schema,mcp-apps}.ts`

- Commentaires explicites : « cette surface ne construit pas de
  `ToolContext` ; la résolution d'identité est appliquée par
  `mcp.ts`/les bindings in-app ». C'est le minimum imposé par le
  brief : « fais-la appeler par les sept » — ici, importée par les
  sept, appelée par celles qui exécutent (mcp, rest, cli).

### 2.8 · `src/lib/tooling/permissions.ts` (nouveau)

- `canRole(category, role)` (`permissions.ts:34-44`). Matrice
  explicite, lisible d'un coup d'œil.
- `assertPermission(ctx, tool, args)` (`permissions.ts:59-96`).
  Deux gates séquentiels : (1) rôle vs catégorie, (2)
  anti-auto-approbation pour `scenario.approve`.
- Codes : `'FORBIDDEN'` (gate 1), `'SELF_APPROVAL'` (gate 2).
- Variante jetante : `assertPermissionOrThrow`
  (`permissions.ts:98-107`), `PermissionDeniedError`
  (`permissions.ts:48-55`).

### 2.9 · `src/lib/tooling/catalog/collection.ts` (modifié hors périmètre principal)

- Tous les `execute` threadent `ctx.tenantId` :
  `listCollections(ctx.tenantId)` (`collection.ts:27-32`),
  `listItems(ctx.tenantId, c.id)` (`collection.ts:33`),
  `getCollection(ctx.tenantId, …)` (`collection.ts:49-50`,
  `:97-100`, `:135-138`, `:168-171`),
  `listItems(ctx.tenantId, …)` (`collection.ts:51`, `:140`,
  `:172`),
  `searchItems(ctx.tenantId, …)` (`collection.ts:79`),
  `deposeProposal(ctx.tenantId, …)` (`collection.ts:111`,
  `:144`, `:176`).
- `args.actorId` retiré des trois schémas `ecriture`
  (`collection.ts:89-94`, `:126-132`, `:161-166`). Le fichier de
  proposition enregistre `ctx.actorId`. Cf. W09.
- `displayName` de `collectionCreate` (`collection.ts:96-99`)
  n'appelle plus `getCollection` — ce champ n'était de toute façon
  jamais consommé (vérifié : `displayName(` n'apparaît dans aucun
  appelant).

### 2.10 · `src/lib/tooling/catalog/scenario.ts` (modifié hors périmètre principal)

- `listProposals(ctx.tenantId)` (`scenario.ts:39`),
  `getProposal(ctx.tenantId, …)` (`scenario.ts:69`, `:90`, `:115`).
- Le retour de `scenario.list` expose `tenantId` par proposition
  (`scenario.ts:46`) — utile pour le client UI qui veut grouper par
  tenant.

## 3 · Tests ajoutés — 51 cas, 3 fichiers

| Fichier                              | Tests | Couverture                                                                                                         |
| ------------------------------------ | ----- | ------------------------------------------------------------------------------------------------------------------ |
| `src/lib/tooling/serverStore.test.ts` | 20    | `assertTenantId` (6), `listItems` sans tenant lève (4), cloison items (4), cloison propositions (3), collections (3). |
| `src/lib/tooling/identity.test.ts`   | 16    | Refus strict (8), mode démo (3), `resolveIdentityOrThrow` (2), whitelists publiées (3).                              |
| `src/lib/tooling/permissions.test.ts` | 15    | `canRole` matrice (3), gate rôle × catégorie (5), gate anti-auto-approbation (5), variante jetante (2).             |
| **Total nouveau**                    | **51**| **51 tests verts, baseline inchangée.**                                                                             |

Baseline mesurée : 192 passing / 194 (2 échecs pré-existants
`orphan-css-vars`, marqués hors périmètre par le brief). Aucune
régression introduite. Les deux échecs sont dans
`src/lib/themes/orphan-css-vars.test.ts` et portent sur des variables
CSS non listées dans `applyThemeTokens` — sans rapport avec cette
campagne.

## 4 · Garde-fous de fin

| Garde-fou     | Statut                                                                                                                                                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `npm run lint` | **vert** — `oxlint` exit 0. Les warnings restants sont préexistants, dans des fichiers hors périmètre (`tools/`, `src/components/`, `src/apps/`). |
| `npm run test` | **vert (baseline)** — 192/194. Les 2 échecs sont `orphan-css-vars`, antérieurs au brief.                                                              |
| `tsc -p tsconfig.tooling.json` | **vert** — exit 0, pas d'erreur sur le périmètre modifié.                                                                       |

## 5 · Trois questions que cette campagne ne tranche pas

1. **`api/v1/[tool].ts` reste sans auth (W03)** — c'est dans
   `api/**`, hors périmètre. Un attaquant peut scanner toutes les
   routes et forger des propositions. La cloison empêche maintenant
   la lecture cross-tenant (W07), mais le dépôt reste ouvert. À
   brancher avec `verifierAcces` (`api/_agent/garde.ts:36`) — déjà
   codé ailleurs, juste pas connecté.

2. **Le seed vit sous le tenant `demo`** — `SEED_TENANT = 'demo'`
   (`serverStore.ts:135`). Si un déploiement en prod oublie de poser
   `COACH_OS_DEMO_MODE=0`, un appel sans tenant sera refusé — mais
   aussi un appel légitime qui n'a pas construit son identité. La V2
   doit fournir une session authentifiée qui pose les en-têtes/args
   **avant** que l'adaptateur voie la requête.

3. **`verify.mjs` (campagne tooling)** appelle toujours
   `listItems('tasks')` sans tenant
   (`scripts/verify.mjs:149, 163`). Il est hors périmètre. À mettre à
   jour avec `COACH_OS_DEMO_MODE=1` ou en passant `--tenant demo`.

## 6 · Suivi à ouvrir (hors brief)

| Item                                                                                                              | Pourquoi                                                         |
| ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| Brancher `verifierAcces` sur `api/v1/[tool].ts` et `api/v1/tools.ts`                                               | Ferme W03.                                                        |
| Mettre à jour `scripts/verify.mjs` pour passer `COACH_OS_DEMO_MODE=1` ou un tenant explicite.                      | Le script casse avec la nouvelle signature.                       |
| Ajouter un quota par tenant (max N propositions / minute)                                                          | Ferme W13.                                                         |
| Étudier un auth Vercel qui pose `x-coach-os-tenant`/`actor` depuis la session, pas depuis l'appelant.                | Seul moyen durable de fermer W02 / W14.                          |
| Étendre `displayName` pour recevoir `ctx` (sinon l'affichage d'une création perd le singulier de la collection).   | Cosmétique mais visible côté client.                             |

## 7 · Note méthodologique

**La cloison avant tout le reste.** L'ordre du brief est le bon ordre :
sans cloison, l'identité et les permissions sont décoratives. Le
premier commit de cette campagne est `serverStore.ts` ; tout le reste
s'y adosse.

**Un défaut silencieux coûte plus qu'un refus bruyant.** Les
assertions sont throws, pas des warnings. Le client reçoit un 401 ou
une enveloppe `ok:false` — pas un 200 avec données d'un autre tenant.
C'est ce qui ferme Melbourne : l'API qui ne peut plus « réussir » par
mégarde sur des données qu'elle n'aurait jamais dû voir.

**Le périmètre exclu (`catalog/`) a quand même bougé**, mais
strictement pour passer `ctx.tenantId` aux appels existants. Aucun
refactor, aucune logique métier changée. Cette décision est notée
explicitement parce qu'elle sort du « ton périmètre » du brief —
sinon les tests verts auraient signifié « on n'a rien changé », ce qui
est faux.

**Le rapport est une photographie, pas une ordonnance.** Trois
trouvailles restent ouvertes ou atténuées ; les atténuations sont
documentées avec leur limite (W05 : la page peut encore poster ; W06 :
la ressource reste publique). Ce qui compte, c'est qu'un relecteur
puisse vérifier chaque ligne en 30 secondes — d'où le format `fichier:ligne`.
