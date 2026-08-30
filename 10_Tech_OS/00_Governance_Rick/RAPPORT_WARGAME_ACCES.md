---
id: WARGAME_ACCES
chantier: gouvernance Rick — audit adversarial
date: 2026-08-14
---

# RAPPORT_WARGAME_ACCES — l'agent qui désinscrit un autre client

## 0 · Périmètre et méthode

Dépôt audité (lecture seule absolue) :

```
omk/repos/coach-os/
  src/lib/tooling/        adapters, catalog, serverStore, ui/
  src/lib/cms/            cms.store.ts, repository.ts
  src/stores/             scenarios.store.ts, tenant.store.ts
  api/                    chat.ts, agent/invoke.ts, v1/[tool].ts, v1/tools.ts, _agent/garde.ts
```

Hors périmètre (non lu) : le câblage in-app côté navigateur (`catalog/_bind.ts`,
`src/agent/scenarios.ts`, `src/agent/tools.ts`). Ces modules reçoivent le
`ToolContext` que les adaptateurs construisent ; ce qu'ils en font — appliquer
sans clic humain un `scenario.approve` ? — changerait la gravité de W12. Le
brief ne les couvrait pas, je ne les ai donc pas lus.

Méthode : un seul agent, lecture statique des fichiers, **aucun appel réel**
ni `curl` contre un serveur vivant. Pas de modification de coach-os. Les
scénarios d'attaque sont des scripts reproductibles, pas des exploits
exécutés.

Trouvailles détaillées dans `wargame_acces.json`. Le présent rapport est
l'argumentaire.

## 1 · Usurpation d'identité — confirmation et extension

Le défaut donné en point d'entrée est à `src/lib/tooling/adapters/mcp.ts:104-113` :

```ts
const ctx: ToolContext = {
  tenantId:
    (args && typeof args === 'object' && '__tenantId' in args
      ? String((args as { __tenantId?: unknown }).__tenantId)
      : null) ?? DEFAULT_TENANT,
  actorId:
    (args && typeof args === 'object' && '__actorId' in args
      ? String((args as { __actorId?: unknown }).__actorId)
      : null) ?? DEFAULT_ACTOR,
};
```

Confirmé, mot pour mot. Le `ctx.tenantId` et le `ctx.actorId` que reçoit
`tool.execute(args, ctx)` viennent **intégralement des arguments JSON-RPC**.
Aucun jeton, aucune session, aucun header, aucune vérification. C'est la faille
de Melbourne : l'autorisation vient de la revendication du client.

### La chaîne jusqu'au store

`collection.read` (catalog/collection.ts:39-66) appelle `getCollection` puis
`listItems(args.collectionId)` — tous deux dans `serverStore.ts`.

`serverStore.ts` charge ses données depuis un **singleton process-global** :

```ts
let _state: ServerState | null = null;
function load(): ServerState { ... _state = { collections, items }; ... }
```

Aucun champ `tenantId` dans `CmsItem`. Aucun filtre dans `listItems` (ligne 149),
dans `getCollection` (ligne 145), ni dans `searchItems` (lignes 166-198). Le
singleton est partagé entre tous les appels, tous tenants confondus. Le `ctx`
reçu par l'executeur n'est **jamais lu** par le serverStore.

**Conséquence pour W07** : `collection.read clients` rend `ava-chen`,
`marcus-reyes`, et tous les clients ajoutés par n'importe quel tenant, sans
égard au `__tenantId`. Le filtrage par tenant que le navigateur fait
correctement dans `cms.store.ts:139-148` (`rebuildFlatView` depuis
`itemsByTenant[activeTenantId]`) **n'existe pas côté serveur**. Le commentaire
en serverStore.ts:7-10 l'admet : « la V2 lira Supabase par tenant, et ce
fichier est l'endroit qui changera ». Tant que la V2 n'est pas déployée, le
filet est troué.

### Confirmation par extension : le client MCP peut aussi écrire

`collection.create/update/delete` (catalog/collection.ts:85-186) appellent
`deposeProposal(...)`. Cette fonction (serverStore.ts:223-246) écrit un
fichier JSON dans `_briefs/.../proposals/` avec `scenarioId` calculé en
ligne 107 de collection.ts :

```ts
const scenarioId = `scn_${ctx.tenantId}_${Date.now().toString(36)}`;
```

Le `ctx.tenantId` est, on l'a vu, ce que l'appelant a déclaré. Donc l'attaquant
qui pose `__tenantId: 'victim-coach'` produit une proposition dans le
namespace `scn_victim-coach_*` — c'est-à-dire dans la file d'approbation
visuelle de la victime. La victime verra « Supprimer Client : Ava Chen »
attribué à `agent:victim` (ou à ce que le payload `actorId` a prétendu). Si
elle approuve, elle supprime sa propre cliente — Melbourne, transposé.

**Un attaquant peut en plus forger l'actor.** Le champ `actorId` est dans le
schéma Zod de `collection.create/update/delete` (collection.ts:93,133,165).
La valeur est utilisée telle quelle (lignes 117,150,182) :
`actorId: args.actorId ?? ctx.actorId`. L'attaquant court-circuite donc
l'identité du ToolContext. W09.

## 2 · Comparaison des sept surfaces

| Surface | D'où vient le tenant | D'où vient l'acteur | Vérif ? | Gravité |
|---|---|---|---|---|
| **mcp** (adapters/mcp.ts:104-113) | `args.__tenantId ?? 'demo'` | `args.__actorId ?? 'agent:mcp'` | aucune | critique |
| **rest** (adapters/rest.ts:31-35) | `header x-coach-os-tenant ?? 'demo'` | `header x-coach-os-actor ?? 'agent:rest'` | aucune — header non signé | critique |
| **cli** (adapters/cli.ts:131-134) | `opts.tenantId ?? 'demo'` | `opts.actorId ?? 'agent:cli'` | aucune (drapeau argv) | sérieux |
| **in-app** (adapters/in-app.ts) | fourni par le binding (runtine navigateur) | idem | dépend du binding | hors périmètre |
| **skill** (adapters/skill.ts) | n/a — génère des fichiers statiques | n/a | n/a | mineur |
| **mcp-apps** (adapters/mcp-apps.ts:138-156) | `args.__tenantId` injecté par le JS du bac à sable | idem | aucune (le bac à sable isole le DOM, pas le payload) | critique |
| **REST v1 routes** (api/v1/[tool].ts:20-35, api/v1/tools.ts) | hérité de l'adaptateur REST | idem | **pas de `verifierAcces`** alors qu'il existe dans `api/_agent/garde.ts:36` | critique |

**Le pattern est uniforme.** Toutes les surfaces prennent l'identité comme un
paramètre de surface — header, flag, champ JSON. Aucune ne la *vérifie*.
Trois conséquences s'ensuvent :

1. **Le serveur n'a aucune source d'autorité sur l'identité.** Quel que soit
   le câblage qu'on ajouterait plus tard, l'identité doit venir d'ailleurs —
   cookie de session, JWT signé, mTLS. Les adaptateurs ont parié le contraire.
2. **La surface la plus exposée au réseau (REST) a perdu son seul filet** :
   `verifierAcces` existe dans `api/_agent/garde.ts:36` mais n'est branché que
   sur `api/chat.ts:48` et `api/agent/invoke.ts:57`. `api/v1/[tool].ts` et
   `api/v1/tools.ts` l'ignorent. Sur un déploiement Vercel, ces deux routes
   sont les portes d'entrée du système — et elles sont ouvertes.
3. **L'asymétrie entre les surfaces cache la faille.** Le commentaire en
   rest.ts:30 dit « côté Vercel, ce sera posé par l'auth ». Une assertion
   identique revient dans le commentaire de l'adaptateur CLI. Chaque surface
   reporte la responsabilité sur l'auth. Aucune ne la porte.

## 3 · L'app en bac à sable — la porte que j'ai écrite hier

`mcp-apps.ts:138-156` injecte dans chaque page le pont JSON-RPC minimal :

```ts
window.pont = {
  initialiser: () => envoyer('ui/initialize', { ... }),
  appelerOutil: (name, args) => envoyer('tools/call', { name, arguments: args || {} }),
  dire: (text) => envoyer('ui/sendMessage', { text }),
};
```

La fonction `appelerOutil` accepte `args` et les poste tels quels vers le
parent. Le parent, qui est aussi l'hôte MCP, relaie vers `mcp.ts:78-141`,
qui lit `args.__tenantId` et `args.__actorId` (lignes 105-112). Donc oui —
**une page rendue dans le bac à sable peut poser `__tenantId: 'victim'` et
`__actorId: 'agent:victim'`**. C'est la même faille que W01, mais livrée clé
en main par notre propre UI.

Le bac à sable protège le DOM parent. Il ne nettoie pas le payload.

Une attaque concrète :

1. L'attaquant rend la page de la file d'approbation via `ui://coach-os/approbations`
   (ce qui est légitime — la page est publique dans `listerRessourcesUi`).
2. Le JS de la page appelle `window.pont.appelerOutil('collection.create',
   {__tenantId:'victim', __actorId:'agent:victim', collectionId:'clients',
   fields:{name:'Inconnu', segment:'X', ticket:0, status:'Active'}, rationale:'...'})`.
3. Une proposition est déposée. La victime, qui ne sait pas que cette page
   a été chargée par un tiers, voit l'entrée dans sa file.

Le code qui appelle `appelerOutil` vit dans la même page (`htmlApprobations`,
ligne 130). Cette page, elle, ne fait que `appelerOutil('scenario.list', {})`
puis `appelerOutil('scenario.approve', {proposalId: id})`. Mais l'attaquant
n'est pas obligé d'utiliser notre HTML — il peut poster un message arbitraire
au parent (le bac à sable permet les `postMessage` au parent), pourvu qu'il
ait un moyen de faire tourner son propre JS dans l'iframe. Or l'iframe charge
du HTML servi par `tool.ui.html()`, qui est généré par le serveur. Si l'HTML
vient de notre code, on contrôle ce qu'il fait. **Mais** : si l'attaquant
parvient à inliner du JS dans le HTML servi (via un outil mal codé dont le
`ui.html()` retourne du contenu forgé), ou simplement via un tool dont l'HTML
contient un point d'injection, il a une machine à forger à la demande.

Le test `mcp-apps.test.ts:11` vérifie qu'aucune URL externe n'apparaît dans
le HTML — bon réflexe. Mais aucun test ne vérifie que `appelerOutil` filtre
ou nettoie ses arguments. W05.

## 4 · L'irréversible — où sont les gardes, et où sont-elles absentes

Inventaire des outils à effet non annulable, et position de leur garde.

| Outil | Effet | Garde | Position | Verdict |
|---|---|---|---|---|
| `collection.create` | Écrit une proposition dans `_briefs/.../proposals/` | aucune — pas de rate limit, pas de quota par tenant | serveur (manquant) | côté serveur, **absente** |
| `collection.update` | idem | idem | idem | idem |
| `collection.delete` | idem | idem | idem | idem |
| `scenario.list` | Lit toutes les propositions, tous tenants | aucune | serveur (manquant) | absente — W10 |
| `scenario.read` | Lit une proposition précise par id | aucune | serveur (manquant) | absente — W11 |
| `scenario.approve` | Rend une instruction d'approbation | refus d'auto-appliquer côté serveur (catalog/scenario.ts:79-102, ligne 98 « Aucun système ne doit auto-appliquer ») | serveur | OK côté serveur, **dangereux côté client** si W12 est vrai |
| `scenario.reject` | Rend une instruction de rejet | idem | serveur | idem |
| `app.open`, `section.goto` | Instruction de navigation | aucune | serveur | effet visuel uniquement, non persistant — non listé comme critique |
| `collection.read` (accès cross-tenant) | Lit les données d'un autre tenant via serverStore singleton | aucune | serveur (manquant) | **W07**, la fuite de données la plus grave |

**Le constat est sans appel.** Tous les outils de la catégorie `ecriture`
ont leur garde **côté serveur**, mais c'est une garde de **proposition**, pas
de **mutation**. Le serveur refuse de muter ; il écrit un fichier. La garde
qu'on cherche — limiter qui peut déposer, plafonner le nombre, vérifier que
l'auteur est bien l'auteur — **n'existe pas**. Les propositions s'empilent.

Et les outils de la catégorie `lecture` (`collection.read`, `collection.search`)
n'ont **aucune** garde sur le tenant. Le singleton `_state` est partagé.
W07.

## 5 · La file d'approbation — Melbourne, à la lettre

Le scénario, rejoué pas à pas contre coach-os.

**Étape 1 — reconnaissance.** L'attaquant (un agent tiers, ou un humain via
le MCP) lit `scenario.list`. W10 : il voit toutes les propositions en
attente, **tous tenants confondus**. Le format `p_<base36-ts>_<rand4>` est
prévisible (la base36 d'un timestamp ms est ~8 caractères, le rand 4), donc
énumérable.

**Étape 2 — usurpation silencieuse.** L'attaquant dépose une proposition
avec `__tenantId: 'victim-coach'`, `__actorId: 'agent:victim'`, et un
contenu inoffensif en apparence (« Mettre à jour la couleur de l'app
Finance en orange »). W08 + W09. La proposition atterrit dans la file de la
victime, signée par `agent:victim`. La victime, qui voit passer des dizaines
de petites propositions par jour, approuve machinalement. Si le client
in-app applique cette approbation automatiquement (ce que je n'ai pas pu
vérifier — voir question ouverte 1), l'attaquant a maintenant la capacité de
modifier **n'importe quel setting** sous couvert de l'identité de la
victime.

**Étape 3 — frappe.** L'attaquant dépose une proposition de suppression
(`collection.delete clients ava-chen`) ou de modification (`collection.update
finance pipeline ticket:0`). W08. La victime voit l'entrée, l'attribue à son
agent interne, approuve. La cliente est supprimée.

**Ce qui rend l'attaque Melbourne-comparable.** À Melbourne, l'agent n'avait
pas à deviner un mot de passe, à contourner un WAF, à exploiter une injection
SQL. Il a juste appelé `cancel_booking(autre_id)` et le serveur l'a laissé
faire. Ici, l'attaquant appelle `collection.delete` avec le bon
`__tenantId` et le serveur l'a laissé faire. La sophistication est
identique : zéro. Le résultat est identique : une action destructive sur les
données d'autrui.

**Ce qui rend la situation coach-os *pire* que Melbourne.** Melbourne
avait un système *centralisé* où la défense devait être sur le serveur.
Coach-os a des outils *distribués* (six surfaces) et un store serveur qui
*admet* ne pas faire de filtre tenant. La surface d'attaque est plus large
et la défense est plus mince.

**Le seul vrai gardien**, c'est l'humain qui approuve. Et l'attaquant a
pris soin de fabriquer des propositions qui ressemblent à celles de l'agent
interne de la victime — `actorId: 'agent:victim'`, libellés plausibles.
L'humain est trompé, pas le serveur.

## 6 · Surface la plus faible

**REST.** Pourquoi.

1. **Seule surface réseau exposée par construction.** MCP tourne en stdio
   sur la machine de l'utilisateur ; CLI aussi ; in-app est dans le même
   navigateur ; mcp-apps est dans une iframe sur la même origine. REST est
   la seule qui *doit* répondre à du trafic non fiable.
2. **Asymétrie d'auth.** `verifierAcces` existe et est branché sur
   `api/chat.ts` et `api/agent/invoke.ts`. Il **ne l'est pas** sur
   `api/v1/[tool].ts:20-35` ni `api/v1/tools.ts:11-17`. C'est un portier
   dans le couloir, et les deux routes qui mènent à la salle des serveurs
   sont sans porte.
3. **Le portier ne porte pas l'identité non plus.** Même si on branchait
   `verifierAcces`, l'identité qui circule reste `x-coach-os-tenant` /
   `x-coach-os-actor`, des en-têtes que le client forge. L'auth dit « tu as
   le droit de parler », pas « tu es qui tu prétends ». La V2 doit résoudre
   les deux.
4. **Pas de rate limit, pas de quota.** W13. 1000 propositions = 1000
   fichiers. Aucun plafond.

**MCP-apps arrive deuxième.** La faille W05 est la même, mais elle demande
à l'attaquant d'avoir une surface pour faire tourner son JS — typiquement, le
navigateur de la victime. C'est moins exposé que REST.

**CLI est sérieux mais contingent.** Le shell est déjà une compromission
totale. Si un attaquant peut passer `--tenant victim-coach`, il peut aussi
passer `cat /etc/passwd`. La gravité « sérieux » plutôt que « critique »
parce que la surface CLI requiert un accès shell préalable.

**MCP pur (stdio) est le moins exposé**, parce qu'il s'exécute dans le
process de l'hôte MCP qui le lance. Mais la faille W01 reste réelle : un
hôte MCP *piraté* (par XSS, par plugin malveillant) hérite du défaut sans
savoir que la donnée qu'il lit vient d'un autre tenant.

## 7 · Tableau des trouvailles, trié par gravité

| ID | Titre court | Surface | Cote | Gravité |
|---|---|---|---|---|
| W01 | Identité déclarée par l'appelant MCP | mcp | interface | critique |
| W02 | Identité déclarée par l'appelant REST | rest | interface | critique |
| W03 | Aucune auth sur /api/v1/* | rest | interface | critique |
| W05 | L'app MCP Apps forge son propre tenant | mcp-apps | interface | critique |
| W07 | serverStore : aucune partition par tenant | mcp | interface | critique |
| W08 | scenarioId forgé dans la file du voisin | mcp | interface | critique |
| W09 | actorId forgé côté schéma | mcp | interface | critique |
| W14 | L'identité forgeable remonte jusqu'au scénario | mcp | interface | critique |
| W04 | Identité déclarée par l'appelant CLI | cli | interface | sérieux |
| W10 | Énumération de la file d'un autre tenant | mcp | interface | sérieux |
| W11 | Lecture d'une proposition précise par id | mcp | interface | sérieux |
| W12 | scenario.approve : instruction sans garde d'auteur | mcp | interface | sérieux |
| W06 | Ressource ui:// lue sans filtre | mcp | interface | mineur |
| W13 | Aucun plafond d'effets de bord par appel | mcp | interface | mineur |

## 8 · Ce que Melbourne aurait donné ici

L'agent de Melbourne avait une tâche banale : réserver un cours. Il a
détruit une réservation d'un tiers parce que l'API ne vérifiait pas *qui*
annulait.

L'agent coach-os a une tâche banale : gérer une collection. Trois issues
équivalentes :

1. **Lecture cross-tenant** — il appelle `collection.read clients`. À cause
   de W07, le serverStore lui rend les clients de tous les tenants. Il ne
   les demandait pas, mais ils sont là. Si l'agent est même vaguement
   attentif aux PII, il vient de recevoir des données qu'il n'aurait jamais
   dû voir — et il les expose dans sa réponse.

2. **Usurpation dans la file d'approbation** — il appelle
   `collection.delete tasks task-42` avec `__tenantId: 'autre-coach'`. À
   cause de W08 + W09, la proposition atterrit dans la file de l'autre
   coach, signée par son actor. L'autre coach approuve, sa tâche est
   supprimée. Même mécanique que Melbourne.

3. **Usurpation par l'UI** — il rend la page d'approbation dans un onglet
   et appelle `window.pont.appelerOutil('collection.create', {__tenantId:
   'autre', ...})`. À cause de W05, la proposition est forgée. Même UI
   qu'il utilise légitimement, payload qui ne l'est pas.

Le point commun : **aucun des trois chemins ne demande à l'agent de
contourner quoi que ce soit.** Il utilise les outils comme ils sont faits.
Les outils sont faits comme si tout le monde était de confiance. Melbourne
avait la même hypothèse — sauf qu'à Melbourne, c'était les humains qu'on
croyait de confiance. Ici, ce sont les agents. Et les agents n'ont pas la
prudence du dernier recours.

## 9 · Ce que le brief sous-estime

Le brief dit « cherche jusqu'où [le défaut] porte, et cherche ses cousins
ailleurs ». Les cousins sont tous là — et le défaut de Melbourne, transposé,
est plus profond que ce que le brief sous-entend.

**Ce que le brief sous-estime**, c'est que le défaut n'est pas seulement
« l'appelant déclare son identité ». C'est aussi « le serveur n'a aucune
identité à vérifier ». `verifierAcces` vérifie que le *caller* est autorisé
à parler. Il ne vérifie pas *qui est le caller* — et il ne pourrait pas, parce
que l'identité qui circule (`x-coach-os-tenant`, `x-coach-os-actor`) est un
claim non signé. La V2 ne peut pas se contenter de poser `verifierAcces` sur
les routes qui l'ont oublié. Elle doit remplacer l'identité auto-déclarée
par une identité inférée d'une session authentifiée.

**Ce que le brief sous-estime aussi**, c'est l'asymétrie d'auth entre les
routes Vercel. C'est l'erreur la plus simple à corriger et la plus
destructrice à conserver : un attaquant n'a même pas à connaître le défaut
de tenant pour tirer parti d'un REST sans auth. Il peut juste scanner
toutes les routes /api/v1/* en boucle et compter les propositions
fabriquées — c'est gratuit pour lui, c'est coûteux pour le propriétaire.

## 10 · Trois questions que la lecture du code ne tranche pas

1. **Le client applique-t-il automatiquement un `scenario.approve` rendu
   via MCP Apps sans geste humain séparé ?** `catalog/scenario.ts:79-102`
   dit explicitement « Aucun système ne doit auto-appliquer ces
   propositions. Le client attend un geste humain. » Mais cette phrase
   décrit une intention. Sans lire le code d'in-app binding (qui vit dans
   `catalog/_bind.ts`, hors périmètre du brief), je ne peux pas affirmer
   qu'aucun chemin n'auto-applique. Si un tel chemin existe, W12 monte en
   critique : un attaquant forge une proposition ET l'approuve dans la
   foulée.

2. **Le serverStore est-il remplacé par Supabase multi-tenant en
   production ?** `serverStore.ts:7-10` dit que oui, dans la V2.
   `cms.store.ts:139-148` montre que la V2 a déjà partitionné les items
   par tenant côté navigateur. Mais le commentaire du serverStore précise
   « ce fichier est l'endroit qui changera » — ce qui veut dire que le
   changement n'est pas encore fait. Si la prod utilise toujours
   serverStore, la fuite W07 est réelle. Si elle lit Supabase avec filtre
   tenant, W07 est corrigé mais W08 reste, parce que `deposeProposal`
   (serverStore.ts:223-246) reste le sink des propositions.

3. **Y a-t-il un middleware Vercel (`middleware.ts` à la racine du projet)
   qui ré-écrit `x-coach-os-tenant` depuis la session ?** Aucun trouvé dans
   le périmètre lu. Si un tel middleware existe hors périmètre, l'impact
   de W02/W03/W04 chute ; les headers forgés seraient écrasés avant
   d'atteindre l'adaptateur REST. Si non, c'est exactement la faille de
   Melbourne, livrée sur REST. C'est la question la plus décisive : elle
   sépare « ce qu'on a écrit est cassé » de « ce qu'on a écrit est cassé
   *et déployé* ».

## 11 · Note méthodologique

Trois points que je veux laisser écrits, parce qu'ils pourraient être lus
comme des hésitations.

**Le défaut de Melbourne est confirmé et étendu**, pas seulement copié.
W01 est le point d'entrée ; W02, W04, W05, W14 montrent qu'il a six
cousins de surface. W07 montre qu'il a un *amplificateur* côté store : le
filtre tenant n'existe nulle part dans serverStore. W08 montre qu'il a
un *vecteur de persistance* : les propositions forgées survivent à la
session, elles attendent une approbation humaine.

**La gravité « critique » est choisie, pas par défaut.** Melbourne a coûté
une réservation. Coach-os peut coûter la suppression d'un client, la
corruption d'une file d'approbation, la lecture de PII cross-tenant. Le
scénario est plus large, l'impact plus haut, le filet plus mince.

**Je n'ai pas proposé de correctif.** Le brief l'interdisait. Les
correctifs vivront ailleurs — `BRIEF_*_CORRECTIFS.md` ou équivalent. Ce
rapport est un diagnostic, pas une ordonnance.
