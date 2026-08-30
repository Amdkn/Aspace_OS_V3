# REPRISE — Agent OS V1, deuxieme session

**Une premiere session a ete interrompue** par une erreur d'API cote MiniMax
(reponse vide en HTTP 200), pas par un defaut de ton travail. Elle a laisse un
socle qui compile et qui s'affiche. Ne recommence pas de zero.

## Ce qui existe deja dans `C:/Users/amado/agent-os/desktop/`

- `src/shell/` — `store.ts`, `Desk.tsx`, `Dock.tsx`, `MenuBar.tsx`, `Window.tsx`
- `src/apps/` — `Observers/`, `Memories/`, `External/`, et `registry.ts`
- `src/storage/` — `contract.ts`, `local.ts`, `pocketbase.ts`, `backup.ts`,
  `useStorage.ts`
- `src/observers.json`, `src/types.ts`, `src/App.tsx`
- Trois dependances seulement : react, react-dom, zustand. **Garde cette
  sobriete.**

**Etat verifie par l'orchestrateur** : `npx tsc --noEmit -p tsconfig.app.json`
rend **0 erreur**, `npm run build` passe (224 Ko), et le bureau s'affiche —
barre de menus, indicateur « Local (IndexedDB) », dock a trois apps.

## Une correction deja faite, a ne pas defaire

`selectOrderedWindows` construisait un nouveau tableau a chaque appel :

```ts
export const selectOrderedWindows = (s) => s.order.map((id) => s.windows[id]).filter(Boolean);
```

`useSyncExternalStore` compare par identite : « getSnapshot should be cached »
puis « Maximum update depth exceeded ». La page ne s'affichait jamais.

Il a ete remplace par le hook `useOrderedWindows()` dans `shell/store.ts`, qui
selectionne `order` et `windows` separement — deux references stables — et derive
avec `useMemo`. Les trois appelants sont a jour. **Ne reintroduis aucun selecteur
qui construit un objet ou un tableau.**

## Ce qu'il reste a faire

1. **Ouvrir une fenetre depuis le dock** et verifier que ca marche. Le bureau est
   vide au premier chargement : rien ne prouve encore que le gestionnaire de
   fenetres fonctionne.
2. **Multi-instances** : deux fenetres de la meme app, deplacables
   independamment.
3. **La persistance** : fermer l'onglet, rouvrir, retrouver son bureau.
4. **L'export et l'import d'instantane** — la fonction qui justifie toute la
   couche durable.
5. **La boucle**, sur chaque ecran. Elle n'a pas encore tourne une seule fois.
6. **Le rapport**, qui n'a pas ete ecrit.

Le brief d'origine suit. Il reste integralement valable.

---

# BRIEF — Agent OS V1 : un bureau web libre, calque sur RyOS

Tu construis **une application neuve**, pas une modification. C'est le
socle d'Agent OS : un bureau web dans lequel on posera ensuite des apps de
toutes sortes.

**Perimetre exclusif : `C:/Users/amado/agent-os/desktop/`** — dossier a creer.
Tu ne modifies rien ailleurs. En particulier `C:/Users/amado/agent-os/observatoire/`
existe deja et **n'est pas a toi**.

## La barre : RyOS

`https://github.com/ryokun6/ryos` · demo vivante `https://os.ryo.lu`

1 221 etoiles, React + TypeScript, **31 apps**, gestionnaire de fenetres
multi-instances, quatre themes d'epoque (System 7, Aqua, Windows XP,
Windows 98), et — le point qui nous interesse le plus — **un systeme de
fichiers virtuel avec persistance locale et sauvegarde/restauration**.

**Les captures sont sur disque** :
`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/barre-ryos/`
Deux vues du bureau. **Ouvre-les.** Tu peux en capturer d'autres :

```
node tools/shot.mjs --url "https://os.ryo.lu" --out /tmp/r.png --wait 12000
```
(depuis le depot coach-os, ou vit `tools/shot.mjs`)

Lis aussi son `README.md` et son `AGENTS.md` sur GitHub. **Tu t'inspires de sa
structure, tu ne le copies pas** : Agent OS n'est pas un hommage retro, c'est un
poste de pilotage d'agents.

## Ce qui rend Agent OS different de Coach OS

Coach OS est un bureau web ferme : 20 apps metier fixes, inscrites dans un
registre. Agent OS doit etre **libre** — on doit pouvoir y poser une app
nouvelle sans toucher au noyau, y compris une app qui n'est qu'un `iframe` vers
une interface existante.

Trois familles d'apps sont prevues, et **tu en livres une de chaque en V1** :

1. **Observateurs** — les onze entrees de
   `C:/Users/amado/ASpace_OS_V3/00_Amadeus/10_Observers/REGISTRY.json` :
   opik, agentpulse, AIOS, agents-observe, phoenix, langsmith, pocketbase-vec,
   super-simple-software-factory, agent-super-spy, observatoire, agent-os.
   **Lis ce registre**, il porte pour chacun son chemin, s'il est present, son
   depot, et parfois sa jonction. L'app les liste, dit lesquels sont installes
   et lesquels sont a cloner.

2. **Memoires** — la couche durable, voir plus bas.

3. **Cadre externe** — une app qui n'est qu'un `iframe` vers une interface qui
   tourne ailleurs. Deux cibles reelles : la console d'**agentgateway**
   (`http://127.0.0.1:15000/ui`) et l'**Observatoire** (`http://127.0.0.1:8787`).
   **Verifie qu'elles repondent avant de promettre quoi que ce soit** : le
   gateway n'est peut-etre pas demarre. Si une cible ne repond pas, l'app doit
   le dire proprement, pas afficher un cadre blanc.

## Les trois couches de stockage

C'est la decision d'architecture de cette V1, et elle est deja prise :

| couche | role | duree de vie |
|---|---|---|
| **Zustand** | etat de session — fenetres ouvertes, focus, position | l'onglet |
| **IndexedDB** | cache local volumineux — vignettes, contenus | le navigateur |
| **PocketBase** | **memoire durable, en fichiers plats** | permanent, exportable |

PocketBase **remplace Supabase** pour Agent OS. Son interet ici est precisement
qu'il stocke en fichiers : on peut **extraire, sauvegarder et prendre des
instantanes locaux** sans passer par un service tiers.

Le binaire existe deja : `C:/Users/amado/pocketbase-vec/` — PocketBase compile
comme cadriciel Go, pilote SQLite WASM (ncruces), extension vectorielle
`sqlite-vec`, **sans CGO**. **Regarde ce qu'il contient et s'il demarre.**

**Ne migre rien, ne demarre aucun service en production.** Pour cette V1 :
- definis le **contrat** de la couche durable — quelles collections, quels
  champs, qui ecrit, qui lit ;
- implemente un **adaptateur** avec deux implementations : une **locale** (fichiers
  ou IndexedDB) qui marche tout de suite, et une **PocketBase** derriere la meme
  interface ;
- livre l'**export et l'import** — un instantane qu'on telecharge et qu'on
  recharge. C'est ce que RyOS appelle backup/restore, et c'est la fonction qui
  justifie tout le reste. Sans elle, la memoire durable n'est pas durable.

## Ce que la V1 doit contenir, et rien de plus

- Un **bureau** : fond, icones, une barre (haut ou bas, ton choix argumente).
- Un **gestionnaire de fenetres** : ouvrir, deplacer, redimensionner, reduire,
  fermer, empiler. **Multi-instances** — deux fenetres de la meme app.
- Un **registre d'apps ouvert** : ajouter une app doit se faire en deposant un
  module, sans editer le noyau. C'est la difference avec Coach OS ; c'est le
  point le plus important de cette V1.
- **Trois apps** : Observateurs, Memoires, Cadre externe.
- La **persistance** : on ferme l'onglet, on rouvre, on retrouve son bureau.
- **Export et import** d'un instantane.

**Pas de theme retro, pas de son, pas de trente apps.** RyOS en a 31 parce qu'il
a des annees ; tu en fais trois qui marchent.

## Le protocole de boucle

Pour chaque ecran :

1. **Construis.**
2. **Photographie** : `node tools/shot.mjs --url "http://localhost:<port>" --out /tmp/a.png`
   Le script liste aussi les erreurs de console.
3. **Juge a l'aveugle** : ta capture a cote d'une capture de RyOS, etiquettes
   retirees. **Une seule question : laquelle des deux tiendrait mieux ?** Pas de
   note sur dix — les notes derivent vers le haut a chaque tour. Un choix, et
   **le seul plus gros ecart**, nomme.
4. Corrige cet ecart. Reprends au 2.
5. Ecran suivant quand la tienne gagne.

Sois dur. Si tu ne peux pas dire laquelle est meilleure, c'est que RyOS gagne.

## Technique

React 19 + TypeScript + Vite + Tailwind v4 + Zustand — meme famille que Coach OS,
pour que le savoir-faire se transfere. `npm create vite@latest`. Les dependances
sont **autorisees ici** (c'est une app neuve, pas l'Observatoire), mais reste
sobre : chaque dependance est une dette.

**Ne reprends pas le code de Coach OS par copier-coller.** Tu peux le lire pour
comprendre un motif — son `AppFrame`, son magasin de fenetres `shell.store.ts`,
son systeme de themes — mais Agent OS doit etre plus libre, pas un clone.

## Interdits

0. **Aucun workflow BMAD** : ils ouvrent une porte « [A] Approve » infranchissable
   en session non interactive.
1. Tu ne modifies **rien** hors de `C:/Users/amado/agent-os/desktop/`. Ni
   l'Observatoire, ni Coach OS, ni les Observers, ni PocketBase.
2. **Jonctions NTFS** : `os.path.islink()` ne les voit pas ; tester
   `FILE_ATTRIBUTE_REPARSE_POINT` (0x400). **Ne supprime jamais une jonction
   autrement que par `os.rmdir`** — `rmtree` et `rm -rf` suivent le lien et
   detruisent la cible. Un parcours naif compte 13,8 millions de fichiers la ou
   il y en a 14 613.
3. Tu ne supprimes rien, nulle part. Pas de `git commit`, pas de `git push`.
4. **Scanne les secrets** avant de citer un fichier — `sk-`, `sbp_`, `vcp_`,
   `ghp_`, JWT, cles PEM, `.env` hors `.example`. Ne recopie aucune valeur.
5. Chemins absolus partout.

## Verification

```
npm run build          # doit passer
npx tsc --noEmit       # 0 erreur : c'est un depot neuf, il n'y a pas de dette a heriter
```

Puis **lance-le et regarde-le**. Ouvre deux fenetres de la meme app, deplace-les,
recharge la page, verifie que le bureau revient. Exporte un instantane,
reimporte-le. **Capture chaque etape.** Une interface validee par lecture de code
est une interface non validee : c'est l'erreur qui a coute le plus cher cette
semaine.

## Rapport

`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/RAPPORT_AGENT_OS_V1.md`

Pour chaque ecran : le nombre de tours, et l'ecart nomme a chaque tour. Puis le
contrat de la couche durable, ce que tu as verifie de PocketBase et du gateway
(repondent-ils, oui ou non), tes captures et ce que tu y as vu, et **tout point
non fait avec sa raison**.

Un point non fait et signale vaut mieux qu'un point bacle en silence.
Si tu dois t'arreter avant la fin, ecris quand meme ce rapport.
