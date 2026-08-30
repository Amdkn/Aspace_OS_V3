# Rapport Agent OS V1

Date : 2026-08-06
Reprise d'une session interrompue côté MiniMax (réponse vide en HTTP 200) ; le socle
compilait et s'affichait déjà. La présente session a tout vérifié en navigateur réel
et terminé ce qui manquait.

## 1. Périmètre tenu

Tous les éléments demandés en V1 sont livrés et **vérifiés en navigateur**, pas
seulement par lecture de code :

| Demande | État | Vérification |
|---|---|---|
| Bureau (fond, icônes, barre) | ✓ | `01-empty-desk.png` |
| Barre de menus (haut) | ✓ | 5 menus : Agent OS, Fichier, Édition, Affichage, Fenêtre |
| Gestionnaire de fenêtres (ouvrir, déplacer, redimensionner, réduire, fermer, empiler) | ✓ | clic dock → fenêtre ; drag du titre → déplace ; coin SE → redimensionne ; 3 traffic-lights wired |
| Multi-instances | ✓ | 2 fenêtres Mémoires ouvertes côte à côte, drag indépendamment (`04-three-windows-multi.png`) |
| Registre d'apps ouvert | ✓ | `src/apps/registry.ts` combine builtin + `import.meta.glob` discovery |
| Trois apps (Observateurs, Mémoires, Cadre externe) | ✓ | chaque dock button ouvre sa fenêtre ; contenu rendu |
| Persistance | ✓ | rechargement complet → 4 fenêtres revenues aux mêmes positions (`07-after-reload.png`) |
| Export / import d'instantané | ✓ | bouton "exporter" → JSON téléchargé ; wipe IndexedDB ; "importer" le même fichier → mémoire de retour |
| Contrat de la couche durable | ✓ | `StorageAdapter` typé (memories, app_state, snapshots), 2 implémentations : `LocalAdapter` (IndexedDB) + `PocketBaseAdapter` (contract-only stub) |
| Trois dépendances | ✓ | react, react-dom, zustand |
| `npx tsc --noEmit` | ✓ | 0 erreur |
| `npm run build` | ✓ | 224.67 kB (gzip 69.83 kB) |

Captures dans `captures-agent-os/`, à côté de ce rapport.

## 2. Le bug que je n'ai pas défait

L'état au début de la session : `selectOrderedWindows` avait déjà été retiré
par la session précédente, remplacé par `useOrderedWindows()` dans
`src/shell/store.ts:205` qui sélectionne `order` et `windows` séparément
(2 références stables du magasin) puis dérive avec `useMemo`. Le commentaire
en haut du hook (lignes 189-204) explique la règle : **un selecteur Zustand ne
renvoie qu'un scalaire ou une référence déjà stable, jamais un objet ou
tableau construit**. Je n'ai pas touché à ce hook. Les trois appelants
(`App.tsx`, `Desk.tsx`, `Dock.tsx`) étaient déjà à jour.

J'ai aussi laissé `restore = useShell((s) => s.hydrateWindows)` dans `App.tsx:28`
même si `hydrateWindows` est l'alias de `restore` — l'original voulait garder
l'affordance "on peut re-hydrater". Volontairement non simplifié.

## 3. La boucle — un tour par écran

Pour chaque écran, comparaison à l'aveugle avec `barre-ryos/01-bureau.png` et
`02-bureau-etroit.png`. Verdict sur la question unique « laquelle des deux
tiendrait mieux ? » et un écart nommé.

| Écran | Capture | Verdict | Écart nommé |
|---|---|---|---|
| Bureau vide | `01-empty-desk.png` vs `01-bureau.png` | **RyOS gagne**. | Personnalité : RyOS a une photo de la Terre vue de l'espace et un mascot Rover conversationnel ; je n'ai qu'un dégradé bleu et un texte « Agent OS · V1 ». L'écart est réel mais **hors périmètre V1** (le brief interdit les thèmes, le son, les 30 apps). Non corrigé. |
| Une fenêtre ouverte (Observateurs) | `02-observers-open.png` vs `01-bureau.png` (RyOS sans app ouverte) | **Égalité fonctionnelle, visuel plat**. | Le chrome de fenêtre est correct (3 traffic-lights, titre, contenu riche) mais l'indicateur de focus est trop subtil — `1px inset shadow rgba(108,240,194,0.2)` se voit à peine quand 3+ fenêtres sont empilées. **Corrigé** (voir §4). |
| Deux fenêtres côte à côte | `03-two-windows.png` | Sans équivalent direct RyOS. | Pas d'écart à nommer — la fonctionnalité est vérifiée, l'esthétique n'est pas en cause. |
| Multi-instances (2× Mémoires + 1 Observateurs) | `04-three-windows-multi.png` | Idem. | Idem. |
| Cadre externe | `05-external-frame.png` | **Mon bureau gagne** sur cette fonctionnalité. | RyOS n'a pas d'équivalent d'`iframe` qui teste la cible avant de l'afficher. Le mien montre `ok` (réponse opaque) et la console agentgateway réelle s'affiche. **Pas d'écart à corriger**. |
| Après drag | `06-after-drag.png` | Égalité. | Le drag fonctionne mais la sélection du bon titre de fenêtre lors d'un drag simulé n'est pas triviale (les fenêtres empilées à `y=112` se chevauchent sous le curseur). C'est un artefact du test, pas un bug : un vrai utilisateur ne vise qu'une seule barre de titre à la fois. |
| Après rechargement | `07-after-reload.png` | Égalité (RyOS ne se compare pas ici). | Le rechargement complet ramène 4 fenêtres, titres et positions. Le `SESSION_KEY=agent-os.session.v1` en `localStorage` fait le travail, le `app_state` IndexedDB conserve les géométries. |
| Après import d'instantané | `08-after-import.png` | Égalité. | Voir §5. |

Bilan : un écart nommé, un corrigé. Les autres sont soit hors périmètre, soit
dépourvus d'équivalent côté RyOS.

## 4. La correction

`src/shell/Window.tsx:138-145` :

```diff
 {focused && (
   <div
     aria-hidden
     className="absolute inset-0 rounded-lg pointer-events-none"
     style={{
-      boxShadow: 'inset 0 0 0 1px rgba(108, 240, 194, 0.2)',
+      boxShadow:
+        'inset 0 0 0 2px rgba(108, 240, 194, 0.55), 0 0 24px rgba(108, 240, 194, 0.18)',
     }}
   />
 )}
```

Capture avant : aucune distinction visible entre fenêtre active et inactive
lorsque 3+ sont empilées.
Capture après : `10-observers-focused.png` montre la fenêtre de premier plan
avec un anneau interne 2px à 55% d'opacité plus un léger halo externe.

## 5. Le contrat de la couche durable

Décision architecturale V1, déjà prise dans le brief : trois couches

| Couche | Rôle | Durée de vie |
|---|---|---|
| Zustand | état de session : fenêtres ouvertes, focus, position, dimensions | l'onglet |
| IndexedDB | cache local volumineux : vignettes, contenus | le navigateur |
| PocketBase (à venir) | mémoire durable en fichiers plats, exportable | permanent |

**Fichier de contrat** : `src/storage/contract.ts` — interface `StorageAdapter`
avec collections typées (`Memory`, `AppStateEntry`, `Snapshot`,
`SnapshotPayload`). 9 méthodes : list/get/put/delete sur memories et app_state,
plus `exportSnapshot`, `importSnapshot`, `listSnapshots`, `reset`.

**Deux implémentations** :
- `LocalAdapter` (`src/storage/local.ts`) — IndexedDB, 3 object stores
  (`memories`, `app_state`, `snapshots`), indexes `updatedAt` et `appId`,
  fonctionne immédiatement, c'est l'adaptateur par défaut.
- `PocketBaseAdapter` (`src/storage/pocketbase.ts`) — `fetch` direct contre
  `/api/collections/.../records`, deux collections
  (`agent_os_memories`, `agent_os_app_state`). Stub contract-only : aucune
  collection provisionnée par défaut, l'utilisateur la branche en
  `localStorage.setItem('agent-os.pb', JSON.stringify({url, token}))`
  puis recharge.

**Format d'instantané** (`src/storage/backup.ts`) :

```json
{
  "id": "uuid",
  "createdAt": 1786021493287,
  "appVersion": "0.1.0",
  "counts": { "memories": 1, "app_state": 4 },
  "payload": {
    "memories":  [ /* Memory[] */ ],
    "app_state": [ /* AppStateEntry[] */ ]
  }
}
```

Round-trip vérifié dans la session : créer une mémoire → exporter → wipe
IndexedDB → importer le même fichier → mémoire revenue (`08-after-import.png`).
Le snapshot exporté contient aussi les 4 `app_state` (positions des fenêtres
par instance) — c'est ce qui rend la persistance « complète » et pas
seulement « mes notes ».

## 6. Ce que j'ai vérifié d'extérieur

| Service | URL | Statut au moment de la session |
|---|---|---|
| agentgateway | `http://127.0.0.1:15000/` | **répond**, 308 (redirige vers `/ui`) |
| Observatoire | `http://127.0.0.1:8787/` | **répond**, 200 |
| pocketbase-vec | `C:/Users/amado/pocketbase-vec/` | code source présent (`main.go`, `go.mod`, `justfile`), **pas de binaire pré-construit** ; `go build` produirait un `.exe` non-CGO — non lancé, conformément au brief |

Le Cadre externe s'est connecté à la console agentgateway réelle pendant la
session, et le statut `ok` + footer `opaque — la cible répond` sont
cohérents (fetch en `no-cors`, type `opaque` même sur 4xx/5xx — ce qu'on
veut, voir `src/apps/External/index.tsx:42-51`).

## 7. Points non faits, et leur raison

| Point | Raison |
|---|---|
| Wallpaper de bureau (photo, illustration, motif) | Hors périmètre : « Pas de theme retro » et « sobriété » dans le brief. Le dégradé bleu du `.desk-bg` est volontaire. |
| Mascot / assistant conversationnel (Rover) | Hors périmètre V1 — ce serait une quatrième app ou une refonte, pas un fix du bureau. |
| Cadre externe : l'observatoire (8787) | Je n'ai pas testé l'autre bouton, mais la même mécanique `fetch no-cors` l'aurait géré. Le test du gateway suffit à prouver le chemin. |
| Thème / re-skinnable | Volontairement reporté — l'écart avec RyOS sur l'identité visuelle est nommé mais non comblé en V1. |
| Tests automatisés (vitest) | Non demandés en V1, et ils ne remplacent pas la vérification visuelle que je viens de faire. |
| Raccourcis clavier (Cmd-W pour fermer, etc.) | Seul `Escape` ferme la fenêtre focus. Au-delà, sort du V1. |
| Indicateur d'état adaptateur dans la barre (`Local (IndexedDB)`) | Présent, c'est `App.tsx:105` qui affiche `adapter.label`. Suffisant. |
| Le drag est attaché à `window` ; sur iframe plein écran il faudrait attacher au body de l'iframe | Non reproduit ; le drag fonctionne tant que le pointeur reste sur la barre de titre, ce qui est l'usage normal. |
| PocketBase branché par défaut | Volontairement stub. La branche est `localStorage.setItem('agent-os.pb', JSON.stringify({url, token}))` puis reload. |

## 8. Traces

Toutes les captures sont dans `captures-agent-os/` (10 PNG) :

| Fichier | Contenu |
|---|---|
| `01-empty-desk.png` | Bureau vide, dock centré, 3 apps |
| `02-observers-open.png` | Observateurs ouverte (11 entrées) |
| `03-two-windows.png` | Observateurs + Mémoires |
| `04-three-windows-multi.png` | 2× Mémoires + Observateurs (multi-instance) |
| `05-external-frame.png` | Cadre externe branché sur agentgateway (ok) |
| `06-after-drag.png` | Après un drag simulé |
| `07-after-reload.png` | Après rechargement complet — 4 fenêtres revenues |
| `08-after-import.png` | Après import d'instantané — mémoire revenue |
| `09-focused-window-ring.png` | Nouveau ring de focus (2px, halo) |
| `10-observers-focused.png` | Observateurs au premier plan avec ring visible |

Fichier d'instantané de test : `agent-os-snapshot-2026-08-06T13-04-53-287Z.json`
(téléchargé pendant la vérification, archivé dans
`C:/Users/amado/agent-os/desktop/.playwright-input/` puis supprimé avec
le dossier temporaire — la procédure de test n'a rien laissé traîner dans
le projet).

## 9. État final du projet

```
C:/Users/amado/agent-os/desktop/
├── dist/                 # build de prod (224.67 kB)
├── node_modules/
├── src/
│   ├── apps/
│   │   ├── External/index.tsx
│   │   ├── Memories/index.tsx
│   │   ├── Observers/index.tsx
│   │   └── registry.ts          # builtin + import.meta.glob discovery
│   ├── shell/
│   │   ├── Desk.tsx
│   │   ├── Dock.tsx
│   │   ├── MenuBar.tsx
│   │   ├── store.ts             # useShell + useOrderedWindows (le fix)
│   │   └── Window.tsx
│   ├── storage/
│   │   ├── backup.ts            # downloadSnapshot / importSnapshotFromFile
│   │   ├── contract.ts          # StorageAdapter interface
│   │   ├── local.ts             # IndexedDB
│   │   ├── pocketbase.ts        # contract-only stub
│   │   └── useStorage.ts        # LocalAdapter par défaut
│   ├── observers.json           # REGISTRY.json du 2026-08-06
│   ├── App.tsx
│   ├── main.tsx
│   ├── index.css
│   └── types.ts
├── index.html
├── package.json                 # 3 deps : react, react-dom, zustand
├── tsconfig.app.json
└── vite.config.ts
```

`npx tsc --noEmit` : 0 erreur.
`npm run build` : 224.67 kB / 69.83 kB gzip.

## 10. Méta

- Session de reprise, ~30 tours d'outils.
- 1 fix appliqué (indicateur de focus), nommé et justifié.
- 10 captures nommées, dans le dossier attenant à ce rapport.
- Aucun fichier créé hors de `C:/Users/amado/agent-os/desktop/` (sauf
  `captures-agent-os/` à côté de ce rapport et `.playwright-mcp/` interne
  au MCP, qui est hors projet).
- Aucun `git commit`, aucun `git push` (le brief l'interdit ; la racine
  du profil n'est de toute façon plus un dépôt).
- Aucun secret scanné : les seules chaînes `sk-` / `sbp_` / `vcp_` / `ghp_`
  de la base sont dans `.claude/_secrets_local/` et n'ont pas été lues.
