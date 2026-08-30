# RAPPORT H — Le tableau des écarts, remesure sur le code d'aujourd'hui

**Date de mesure** : 2026-08-13
**Date du tableau original** : 2026-08-07 (écrit dans `ARCHITECTURE_V1.md` § « Tableau des écarts »)
**Dépôt mesuré** : `repos/coach-os` (HEAD de travail, non touché)
**Périmètre de mesure** : `src/lib/cms/`, `src/lib/tooling/`, `src/agent/`, `src/stores/`, `src/apps/`, `cli/`, `mcp/`, `coach-os-plugin/`, `package.json`

---

## 1. Méthode

Six lignes à remesurer. Pour chacune : recopie de l'affirmation d'origine, mesure sur le code (avec `fichier:ligne`), verdict (`CONFIRME` · `PERIME` · `PARTIEL`), et ligne corrigée.

Trois mesures chiffrées en plus :

- combien d'outils via `defineTool` ;
- combien d'apps ont un bouton de création ;
- état de `npm run test` et `npm run build`.

Sortie : la question qui vaut plus que le tableau — quel est le premier rang réellement non posé ?

**Aucune écriture dans `repos/coach-os/**`. Aucune modification de `ARCHITECTURE_V1.md`.** Mesures seulement.

---

## 2. Tableau corrigé — six lignes

| rang | verdict | ce que le code dit (résumé) |
|---|---|---|
| 0 | **PERIME** | `addItem` / `removeItem` (+ `addItemFor` / `removeItemFor`) sont dans `cms.store.ts` ; 11 apps sur 19 ont un bouton de création routé via `addItem` ; applicateurs en place avec revert. |
| 1 | **PARTIEL** | scénarios + approbation + tests merge 3 propositions en place. Manque : test d'idempotence (`approveAndMerge` ne garde pas contre un double appel) ; code de confirmation Lumail 6 chiffres pour outils à effet de bord externe — zéro dans la codebase. |
| 2 | **CONFIRME** | pas de `langgraph` dans `package.json`, pas d'import `StateGraph` dans `src/`. Tour de boucle uniquement. |
| 3 | **PERIME** | serveur MCP stdio multiplexe existe : `mcp/server.ts` (14 lignes) + `mcp/server.mjs` (build) + `src/lib/tooling/adapters/mcp.ts` (128 lignes), déclaré dans `coach-os-plugin/mcp.json`. |
| 4 | **PERIME** | les 6 adaptateurs sont là : `cli.ts`, `in-app.ts`, `mcp.ts`, `mcp-schema.ts`, `rest.ts`, `skill.ts`. Binaire `coach-os` déclaré dans `package.json` (`bin: ./cli/coach-os.mjs`). Doc one-shot dans `coach-os-plugin/skills/INSTALL.md`. |
| 5 | **PERIME** | `coach-os-plugin/` est en place : `plugin.json` conforme spec 1.0.0 (name=coach-os, $schema, MIT, extensions), `mcp.json` (1 serveur stdio), 13 `SKILL.md` générés, `INSTALL.md`. |

**Conclusion synthétique** : **cinq lignes sur six du tableau du 2026-08-07 sont périmées** (rangs 0, 3, 4, 5) ou partiellement vraies (rang 1). Une seule est confirmée (rang 2). Construire sur ce tableau comme s'il disait vrai aujourd'hui pousserait à réécrire du code qui existe déjà.

---

## 3. Mesures détaillées par rang

### Rang 0 — Écriture CMS — PERIME

**L'affirmation du 2026-08-07** :
> `createItem` / `deleteItem` dans le CMS (n'existe pas), boutons de création dans les apps (Tasks, etc.), applicateurs pour les nouveaux outils

**Ce que le code dit** :

Le CMS expose quatre opérations CRUD, en deux variantes (active-tenant + multi-tenant) :

- `cms.store.ts:77` — interface `addItem: (collectionId, partial) => AddItemResult`
- `cms.store.ts:78` — interface `removeItem: (collectionId, id) => { ok, error? }`
- `cms.store.ts:92-101` — variantes tenant-aware `addItemFor` / `removeItemFor`
- `cms.store.ts:252-275` — implémentation `addItemFor` : génère un id `${collection}_${ts}_${rand}`, set optimiste, persistance best-effort via `repoUpsertItem`
- `cms.store.ts:283-316` — implémentation `removeItemFor` : vérifie présence, retire, persistance via `repoRemoveItem`

Les noms sont `addItem`/`removeItem` (pas `createItem`/`deleteItem`) — la convention du dépôt. La fonction `applyCreerItem` côté agent :

- `agent/tools.ts:345-350` — `creerItem` dépose via `addProposal` (pas d'écriture directe)
- `agent/tools.ts:359-373` — `applyCreerItem` capture le résultat de `addItem` et fournit un `revert` qui appelle `removeItem` sur l'id retourné

Le nombre d'apps avec bouton de création routé via `addItem` :

| app | fichier:ligne | collection cible |
|---|---|---|
| Tasks | `apps/tasks/TasksApp.tsx:208` | `tasks` |
| Sales (liste) | `apps/sales/SalesApp.tsx:1630` | `deals` |
| Sales (détail) | `apps/sales/SalesDetailPage.tsx:112,128` | `clients`, `invoices` |
| Sales (item) | `apps/sales/SalesItemDetail.tsx:89,106` | `clients`, `invoices` |
| Clients | `apps/clients/ClientsApp.tsx:83` | `clients` |
| Finance | `apps/finance/FinanceApp.tsx:228` | `invoices` |
| Operations | `apps/operations/OperationsApp.tsx:165,202` | `changes`, `alerts` |
| Growth | `apps/growth/GrowthApp.tsx:306,581` | `growth_acquisition`, `growth_partenariats` |
| IT-RD | `apps/it-rd/ItRdApp.tsx:131,562` | `it_journal`, `it_drift` |
| Cognition | `apps/cognition/CognitionApp.tsx:342` | `ROUTINE_COLLECTION` |
| Product | `apps/product/ProductApp.tsx:505` | `product_mvps` |
| Legal (ProwlerImport) | `apps/legal/ProwlerImport.tsx:109` | `legal_gaps` |
| People (ApprovalsView) | `apps/people/ApprovalsView.tsx:337,361` | `approval_decisions` |

**11 apps sur 19** (audit, auth, dashboard, design, marketplace, onboarding, ontology, settings, welcome — pas de bouton de création ; pour 5 d'entre elles, c'est par design : auth, dashboard, settings, onboarding, welcome n'ont pas de données métier à créer).

**Ligne corrigée** : « Rang 0 globalement couvert : CMS a `addItem`/`removeItem` (+ variantes tenant-aware), 11 apps ont un bouton de création, applicateurs en place avec revert symétrique. Reste : ~8 apps sans bouton — pour certaines par design, pour d'autres un reliquat. »

---

### Rang 1 — Scénarios + approbation — PARTIEL

**L'affirmation du 2026-08-07** :
> `scenarios.store.ts`, `scenarios.ts`, `mergeAtomically` (tout-ou-rien + revert), `ApprovalsView.tsx` (715 lignes, 134 mentions scenario/proposal). Manque : tester le merge sur plus de 2 propositions, tester l'idempotence des reverts, **code de confirmation** style Lumail pour les outils à effet de bord externe (envoi sortant)

**Ce que le code dit** :

- `src/stores/scenarios.store.ts` — fichier présent, 412 lignes (commentaire de tête inclus)
- `src/agent/scenarios.ts:42-126` — `mergeAtomically` (sémantique tout-ou-rien, revert en cascade)
- `src/apps/people/ApprovalsView.tsx` — fichier présent, **952 lignes** (et non 715 — le tableau sous-estime l'évolution)
- `src/agent/scenarios.test.ts:54-86` — test « CAS CRITIQUE » qui utilise **3 propositions** (`incA`, `explode`, `incB`) ; assertion explicite que rien n'a fui après revert
- `src/stores/scenarios.store.test.ts` — 9 tests, dont `approveAndMerge applique les propositions via les applicateurs` et `approveAndMerge qui échoue revert toutes les propositions`

**Ce qui manque réellement** :

1. **Idempotence des reverts** : aucun test ne vérifie qu'`approveAndMerge` appelé deux fois sur le même scénario est no-op. À `scenarios.store.ts:310`, `approveAndMerge` lit `before.proposals` et applique sans vérifier `before.status === 'merged'`. Un double appel ré-appliquerait toutes les propositions. Idem pour `scenarios.ts:62-80` (`mergeAtomically` n'a pas de garde anti-double).

2. **Code de confirmation Lumail 6 chiffres** : recherche globale `confirmationCode | otpCode | sixDigit | 6-digit | toConfirm | confirmCode` → **0 résultat** dans `src/`. Aucune génération de code, aucune modale « entrez le code à 6 chiffres », aucune vérification côté Approvals.

**Ligne corrigée** : « Rang 1 partiellement couvert : scénarios + approbation + tests merge 3 propositions en place. Manque : (a) test d'idempotence des reverts (deuxième appel à `approveAndMerge` doit être no-op) ; (b) `ApprovalsView.tsx` a grandi de 715 → 952 lignes ; (c) **code de confirmation Lumail** pour outils à effet de bord externe — **zéro dans la codebase**, alors que c'est la mesure citée par `ARCHITECTURE_V1 §Risque 1` comme nécessaire pour empêcher l'envoi sortant automatique au nom de la marque. »

---

### Rang 2 — Graphe d'état — CONFIRME

**L'affirmation du 2026-08-07** :
> rien — tour de boucle uniquement

**Ce que le code dit** :

- `package.json` (dependencies + devDependencies) — aucune trace de `@langchain/langgraph`, `langgraph`, `@langchain/core`
- `src/` — recherche `langgraph | StateGraph | stateGraph` → **0 import, 0 usage réel**
- La seule occurrence textuelle est `src/lib/cms/seed.ts:160` : `{ id: 'langgraph-supervisor', title: 'LangGraph supervisor', meta: 'Summers → workers', stage: 'building', notes: 'B1 Summers as supervisor node, dispatching to B2/B3 worker agents via LangGraph.' }` — c'est du contenu CMS (note de planning dans une fiche), pas du code
- `src/agent/` — `tools.ts`, `scenarios.ts`, `voice.ts`, `characters.ts`, `VoiceWave.tsx`, `AssistantOverlay.tsx`. Pas de fichier graphe

**Ligne corrigée** : « Rang 2 confirmé : pas de graphe d'état, tour de boucle uniquement. Mais le tableau est cohérent avec ce constat — c'est la seule ligne qui survit à la remesure. »

---

### Rang 3 — Workflows par MCP — PERIME

**L'affirmation du 2026-08-07** :
> **aucun serveur MCP** dans le dépôt (`grep` confirme)

**Ce que le code dit** :

- `package.json` — `devDependencies."@modelcontextprotocol/sdk": "^1.30.0"`
- `mcp/server.ts` (14 lignes) — entrée du serveur MCP stdio ; délègue à `runMcpStdio` :
  ```ts
  import { runMcpStdio } from '../src/lib/tooling/adapters/mcp';
  runMcpStdio().catch((err) => { ... });
  ```
- `mcp/server.mjs` — version compilée pour lancement Node direct
- `src/lib/tooling/adapters/mcp.ts:11` — `import { Server } from '@modelcontextprotocol/sdk/server/index.js'`
- `src/lib/tooling/adapters/mcp.ts:28-118` — `buildMcpServer()` construit une `Server` officielle (capabilities.tools), branche les handlers `ListToolsRequestSchema` (rend tous les outils via `list()`) et `CallToolRequestSchema` (appelle `tool.execute`)
- `src/lib/tooling/adapters/mcp.ts:122-128` — `runMcpStdio()` connecte un `StdioServerTransport`
- `coach-os-plugin/mcp.json:3-12` — déclare le serveur dans le plugin :
  ```json
  "coach-os": {
    "type": "stdio",
    "command": "node",
    "args": ["${PLUGIN_ROOT}/../mcp/server.mjs"],
    "cwd": "${PLUGIN_ROOT}/.."
  }
  ```

Le serveur MCP multiplexe les 13 outils — conforme à ce que recommande ARCHITECTURE_V1 §4 (« 1 connexion vs N »). La phrase « `grep` confirme » du tableau original est factuellement fausse.

**Ligne corrigée** : « Rang 3 obsolète sur la forme : un serveur MCP stdio multiplexe les 13 outils existe (`mcp/server.mjs` + `src/lib/tooling/adapters/mcp.ts`), est conforme au SDK `@modelcontextprotocol/sdk` 1.30.0, et est déjà déclaré dans `coach-os-plugin/mcp.json`. Reste l'idée n8n self-hosté comme plan, mais c'était un plan, pas un constat. Le vrai manque du tableau d'origine (« pas de serveur MCP joignable ») est faux. »

---

### Rang 4 — Capacités exposées — PERIME

**L'affirmation du 2026-08-07** :
> in-app ✅, Skills partiel (prompt serveur), MCP ❌, CLI ❌, API REST partiel. Manque : adaptateurs (cf. Melvynx) : `defineTool` → MCP, CLI, Skill. Documentation one-shot sur URL publique.

**Ce que le code dit** :

Les **6 adaptateurs** (et un helper) sous `src/lib/tooling/adapters/` :

| adaptateur | rôle | fichier:ligne clé |
|---|---|---|
| `cli.ts` | parse argv, résout outil, format JSON / brief | `cli.ts:39-143` (`runCli`) |
| `in-app.ts` | binding client (delegate vers impl existante) | `in-app.ts:49-50` (`registerInApp`) |
| `mcp.ts` | serveur MCP stdio (cf. rang 3) | `mcp.ts:28-128` |
| `mcp-schema.ts` | `zodToInputSchema` pour JSON Schema | utilisé par `mcp.ts:47` |
| `rest.ts` | handler Web + manifest OpenAPI-ish | `rest.ts:40-52` (`manifestTools`) |
| `skill.ts` | génère `skills/<outil>/SKILL.md` | `skill.ts:21-29` (`buildSkill` + `buildAllSkills`) |
| `zod-introspect.ts` | helper introspection Zod (pas un adaptateur) | — |

Le binaire CLI :

- `package.json:6-8` — `"bin": { "coach-os": "./cli/coach-os.mjs" }`
- `cli/coach-os.mjs:11-18` — `runCli({argv: process.argv, color: ...})` puis exit

La documentation one-shot (cité Melvynx frame 0017 — « paste this into Claude Code ») :

- `coach-os-plugin/skills/INSTALL.md:8-15` — snippets par client :
  ```
  Read coach-os-plugin/plugin.json and install the Coach OS plugin for me.
  ```
  pour Claude Code ; renvoi vers le README du client pour Codex / Cursor / Hermes.

**Ligne corrigée** : « Rang 4 obsolète : in-app, MCP, CLI, REST, Skill sont tous branchés via les 6 adaptateurs, le binaire `coach-os` est dans `package.json`, et la doc one-shot est dans `INSTALL.md`. La mention « documentation sur URL publique » reste partiellement fausse — `INSTALL.md` est versionné dans le dépôt (à `coach-os-plugin/skills/INSTALL.md`), pas sur une URL type `coach-os.com/install`. »

---

### Rang 5 — Agent Plugins — PERIME

**L'affirmation du 2026-08-07** :
> rien

**Ce que le code dit** :

`coach-os-plugin/` est complet :

- `coach-os-plugin/plugin.json` (19 lignes) — manifeste conforme spec 1.0.0 :
  - `$schema: "https://agentplugins.org/schemas/1.0.0/plugin.schema.json"` ✓
  - `name: "coach-os"` ✓ (1–64 chars, kebab)
  - `version: "0.1.0"` ✓ (SemVer)
  - `description` (240 chars, conforme) ✓
  - `author: { name: "OMK Services", url: ... }` ✓
  - `homepage`, `repository`, `license: "MIT"` ✓
  - `keywords: ["coach", "sop", "no-code", "approvals", "agent-skills", "mcp"]` ✓
  - `extensions.claude-code.mcpConfigPath: "mcp.json"` ✓ (extension client)

- `coach-os-plugin/mcp.json` (12 lignes) — un serveur stdio multiplexe « coach-os », args `${PLUGIN_ROOT}/../mcp/server.mjs`, env `COACH_OS_PROPOSAL_DIR=${PLUGIN_DATA}/proposals` (utilisation de `PLUGIN_ROOT` et `PLUGIN_DATA` comme l'exige la spec §3)

- `coach-os-plugin/skills/` — **14 entrées** : 13 dossiers `<outil>/` + `INSTALL.md`. Les 13 dossiers :
  ```
  app.list        app.open        collection.create  collection.delete
  collection.list collection.read collection.search collection.update
  scenario.approve scenario.list   scenario.read      scenario.reject
  section.goto
  ```
  Chacun contient un `SKILL.md` avec frontmatter (`name`, `description`, `category`) + corps (sections « Quand », « Comment », « Erreurs courantes », « Exemples »).

- `coach-os-plugin/skills/INSTALL.md` — doc one-shot + 3 vérifications de fumée (`npx coach-os --help`, `npx coach-os tools list`, `curl POST /api/v1/collection.list`).

**Ligne corrigée** : « Rang 5 obsolète : `plugin.json`, `mcp.json`, 13 `SKILL.md` et `INSTALL.md` sont en place et conformes à la spec Agent Plugins 1.0.0 (avec extension `claude-code`). Ce qui manque éventuellement : publication aux marketplaces (Cursor, VS Code) — c'est une étape de distribution, pas une absence de code. »

---

## 4. Mesures chiffrées

### 4.1 Outils déclarés via `defineTool`

13 outils au total, répartis sur 3 catalogues (`src/lib/tooling/catalog/`).

| catalogue | nombre | outils |
|---|---|---|
| `collection.ts` | 6 | `collection.list`, `collection.read`, `collection.search`, `collection.create`, `collection.update`, `collection.delete` |
| `app.ts` | 3 | `app.list`, `app.open`, `section.goto` |
| `scenario.ts` | 4 | `scenario.list`, `scenario.read`, `scenario.approve`, `scenario.reject` |

**Total : 13 outils.**

### 4.2 Outils avec effet de bord (écriture directe)

**0 outil n'écrit directement dans les données.**

C'est la garantie canonique du projet : les outils de catégorie `ecriture` (`collection.create`, `collection.update`, `collection.delete`) retournent une `ProposalRef` et déposent une proposition. Les outils `scenario.approve` / `scenario.reject` retournent une instruction `clientCommand` à exécuter par un humain via le client.

| catégorie | nombre | comportement |
|---|---|---|
| `lecture` | 6 | retour immédiat, aucun effet de bord |
| `navigation` | 4 | instruction d'affichage (le client applique) |
| `ecriture` | 3 | dépôt de proposition, jamais d'écriture directe |

### 4.3 Apps avec bouton de création (rangé par `addItem`)

**11 apps sur 19** ont au moins un appel `addItem(` (cf. §3, rang 0 pour la liste exhaustive).

### 4.4 État des tests — `npm run test`

```
RUN  v4.1.10 .../coach-os

 Test Files  1 failed | 13 passed (14)
      Tests  2 failed | 136 passed (138)
   Start at  02:46:39
   Duration  49.90s
```

**138 tests, 136 passent, 2 échouent.** Les deux échecs sont dans `src/lib/themes/orphan-css-vars.test.ts` :

1. **22 variables CSS orphelines** : `--landing-text-muted`, `--landing-sans`, `--landing-canvas`, `--landing-text`, `--landing-border-subtle`, `--landing-serif`, `--landing-ink`, `--landing-accent`, `--landing-text-faint`, `--landing-ink-tint`, `--landing-border`, `--landing-surface`, `--landing-radius`, `--landing-shadow`, `--landing-radius-lg`, `--landing-accent-soft`, `--landing-surface-tint`, `--landing-ok-tint`, `--landing-ok`, `--landing-amber-tint`, `--landing-amber`, `--landing-shadow-lift`. Elles sont consommées par `var(--xxx)` mais ni écrites dans `applyThemeTokens` (store.ts:62-104) ni déclarées dans `:root` / `[data-theme]` de `src/index.css`, ni ajoutées à `EXCLUSIONS`. Le test échoue sur la garde « tout var(--xxx) consommé est écrit ou exclu ».

2. **Garde-fou REGRESSION_9_ALIAS_REMOVED** : 9 alias story-1 manquent dans `applyThemeTokens` — `--theme-muted`, `--canvas`, `--panel`, `--panel-solid`, `--panel-border`, `--panel-border-subtle`, `--hairline`, `--shadow-panel`, `--shadow-window`. C'est un test de non-régression qui vérifie qu'on n'a pas régressé sur les alias introduits dans la story 1 du thème.

Les deux échecs sont dans le **même fichier** (`orphan-css-vars.test.ts`) et concernent la **même racine** : variables CSS consommées mais pas déclarées. C'est un point CSS/thème, pas un point d'architecture agent ou MCP.

### 4.5 État du build — `npm run build`

```
vite v8.1.5 building client environment for production...
✓ 2526 modules transformed.
dist/index.html                                 0.47 kB │ gzip:   0.30 kB
dist/assets/solarpunk-default-DtPu5woT.jpg    199.62 kB
dist/assets/index-B07pPZHS.css                126.55 kB │ gzip:  20.08 kB
dist/assets/index-Bg9Sixii.js               2,423.47 kB │ gzip: 628.11 kB

[INEFFECTIVE_DYNAMIC_IMPORT] src/lib/cms/seed.ts is dynamically imported by src/lib/cms/cms.store.ts but also statically imported by src/lib/app-discovery.tsx, dynamic import will not move module into another chunk.

⚠ Some chunks are larger than 500 kB after minification.

✓ built in 4.96s
```

**Build réussi en 4.96 s.** Avertissements (non bloquants) : un dynamic import ineffectif (déjà statiquement importé ailleurs) et un bundle JS > 500 kB. À noter pour la suite mais n'invalide rien.

---

## 5. Le premier rang réellement non posé

**C'est le rang 1.**

Le code de confirmation Lumail à 6 chiffres — cité par `ARCHITECTURE_V1 §2` (frame 0090) et `§Risque 1` comme **le mécanisme qui empêche un incident de portée production** — **n'existe nulle part** dans la codebase. Le contrat « les outils `ecriture` déposent une proposition, jamais d'écriture directe » tient au niveau du code agent (`collection.create/update/delete` retournent une `ProposalRef`, `applyCreerItem` symétrique avec revert), mais **rien n'empêche aujourd'hui un applicateur d'appeler une API externe sortante** — par exemple un futur outil `envoyerMessageLinkedIn` qui appellerait Unipile sans passer par la file. La garde actuelle est *conventionnelle* (le développeur n'écrit pas un outil qui contourne), pas *mécanique* (pas de modale « entrez le code à 6 chiffres » avant d'exécuter).

**Plus précisément, ce qui manque au rang 1 pour que la promesse tienne en production :**

1. **Code de confirmation 6 chiffres** (le Lumail-style) demandé côté `ApprovalsView` au moment d'approuver un scénario contenant un outil à effet de bord externe (marqué, par exemple, `category: 'ecriture' && effectOfSide: 'external'`). Aucun match pour `confirmationCode | otpCode | sixDigit` dans `src/`.

2. **Marqueur des outils à effet de bord externe** dans le catalogue. Aujourd'hui, la distinction `lecture | navigation | ecriture` est interne au workflow d'approbation. Il faut une 4ᵉ catégorie ou un flag `externalEffect: true` pour que `ApprovalsView` sache qu'il faut exiger un code avant de laisser passer.

3. **Test d'idempotence** : `approveAndMerge` (`scenarios.store.ts:310`) ne vérifie pas `before.status === 'merged'` avant d'appliquer. Un double appel ré-appliquerait toutes les propositions. Idem côté `mergeAtomically` (`scenarios.ts:62-80`). Le test d'idempotence serait une ligne (`if (scenario.status === 'merged') return scenario;`) plus une assertion.

Les autres manques (rang 0 — 8 apps sans bouton de création ; rang 1 — test d'idempotence seul ; rang 2 — pas de graphe ; rang 3 — n8n ; rang 4 — URL publique vs INSTALL.md versionné ; rang 5 — soumission marketplaces) sont **secondaires** par rapport au risque 1 du tableau d'origines. C'est le rang 1 qui débloque la sortie vers l'extérieur, pas les autres.

---

## 6. Ce que je n'ai pas pu mesurer, et pourquoi

1. **Comportement runtime du serveur MCP**. Le serveur existe (`mcp/server.ts`, `mcp/server.mjs`), les 13 outils sont enregistrés via `registerAll()` (`catalog/index.ts:12-18`). Mais je n'ai pas lancé un agent externe (Claude Code, Codex) et vérifié qu'il négocie `initialize` + `tools/list` + `tools/call` sans erreur. Le test serait : cloner `coach-os-plugin/` dans un projet de test, ajouter le mcp.json à `~/.claude/mcp.json`, et taper « liste les collections ». À faire en local.

2. **Conformité exacte des SKILL.md à la spec Agent Skills 1.0.0**. J'ai vérifié que chaque `SKILL.md` a un frontmatter `name` + `description` + `category`, conforme à la lecture rapide de `spec/1.0.0.md`. Je n'ai pas chargé le validateur officiel (s'il existe) ni vérifié champ par champ que `description` est en prose, `≤ 1024 caractères`, etc.

3. **Exhaustivité de l'adaptateur `in-app.ts`**. Le commentaire de tête dit « ne PAS modifier `src/agent/tools.ts` » — j'ai vérifié que `src/agent/tools.ts` n'est pas modifié par l'adaptateur. Je n'ai pas vérifié que TOUS les 13 outils ont un binding côté client (le fichier `_bindings` est vide par défaut ; il doit être alimenté par `catalog/_bind.ts` que je n'ai pas ouvert ligne à ligne).

4. **Exécution réelle de `coach-os tools list` en CLI**. Le binaire est là (`cli/coach-os.mjs`), le wrapper `runCli` est testé unitairement (je présume — pas vérifié), mais je n'ai pas lancé `node cli/coach-os.mjs tools list` après `npm run tooling:build`. Le test serait : `npm run tooling:build && node cli/coach-os.mjs --version` → devrait rendre `coach-os 0.1.0`. À 30 secondes de manipulation, hors périmètre de ce brief.

5. **État réel de `n8n` côté infra**. Le tableau d'origine parlait de « installer n8n self-hosté ». Je n'ai pas vérifié si une instance n8n tourne quelque part (VM, Docker, Render). C'est en dehors du dépôt `coach-os`, c'est une décision d'infra qui n'a pas de marque dans le code.

6. **Date de la dernière mesure de `ApprovalsView.tsx` à 715 lignes**. Le tableau original cite 715 lignes. Aujourd'hui, le fichier en fait 952. L'écart (715 → 952) représente le travail d'approbation fait entre le 2026-08-07 et aujourd'hui — j'ai constaté l'écart, je ne sais pas exactement quels commits l'ont fait grossir (pas l'objet de ce brief).

7. **Identité exacte de la dépendance `@modelcontextprotocol/sdk ^1.30.0`**. Le tableau d'origine dit « aucune dépendance `@modelcontextprotocol/sdk` ». En fait elle existe, en `devDependencies` (pas en `dependencies`) — c'est peut-être la nuance qui a fait écrire le « grep confirme » à l'envers : la recherche a peut-être été faite dans `dependencies` seule, pas dans `devDependencies`. Hypothèse, pas vérifiée.

---

## 7. Sources

Toutes les preuves sont sourcées `fichier:ligne` dans la section §3 et dans `ecarts_reels.json`. Les mesures chiffrées (§4) viennent de :

- `npm run test` exécuté le 2026-08-13 dans `repos/coach-os/`
- `npm run build` exécuté le 2026-08-13 dans `repos/coach-os/`
- `grep` et `Read` sur les fichiers du dépôt `repos/coach-os/`

Aucun outil tiers, aucun agent délégué. Mesure faite à la main.