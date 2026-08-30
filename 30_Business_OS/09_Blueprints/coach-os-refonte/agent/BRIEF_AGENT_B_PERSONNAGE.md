# AGENT-B — Le personnage

Lis `CONTRAT.md` dans ce même dossier. Il fait partie de ce brief et prime sur lui.

Ton rapport : `RAPPORT_AGENT_B.md`, à côté de ce brief.

---

## Ce qu'on construit

Un personnage animé qui vit sur le bureau de Coach OS, comme Clippy dans RyOS : il apparaît,
il pense, il parle dans une bulle, on le déplace, on en change. C'est la surface visible de
l'agent — le moteur qui répond est construit en parallèle par AGENT-A, derrière `/api/chat`.

## Les planches de sprites sont déjà là

Douze personnages ont été téléchargés dans `public/assets/assistant/<id>/` :

```
clippy  links  rover  merlin  genie  peedy  genius  rocky  f1  officelogo  saeko  monkeyking
```

Chacun a deux fichiers, et **le format est vérifié, pas supposé** :

- `map.png` — la planche, une grille de vignettes.
- `agent.json` — `{ framesize: [w,h], overlayCount: n, animations: { <Nom>: { frames: [...] } } }`

Une frame :

```jsonc
{
  "duration": 100,                    // millisecondes
  "images": [[1984, 2790]],           // un couple [x,y] PAR COUCHE (overlayCount)
  "branching": { "branches": [ { "frameIndex": 30, "weight": 40 } ] },
  "sound": "15"
}
```

Trois choses à ne pas rater :

- **Une frame sans `images` est une frame vide** — le personnage disparaît. C'est voulu : les
  animations d'entrée commencent par des frames vides et le font se matérialiser.
- **`images` a une entrée par couche.** `overlayCount` va de 1 (Clippy) à 3 (Merlin, Genie,
  Peedy). Il faut donc empiler autant de calques, chacun avec sa propre position de fond.
- **`branching` est probabiliste** : `weight` sur 100, le reste continue en séquence.

Les tailles et le nombre d'animations varient : Rover fait 80×80 avec 29 animations, Peedy
160×128 avec 85. Rien ne doit être codé en dur.

## L'inventaire des animations, et l'intention

Les noms d'animations diffèrent d'un personnage à l'autre. Ne code pas `"Thinking"` en dur :
associe une **intention** à une liste de candidats, et prends le premier que le personnage
possède.

| intention | candidats, dans l'ordre |
|---|---|
| entrée | `Greeting`, `Show`, `Appear`, `Entrance` |
| réflexion | `Thinking`, `Think`, `Processing`, `CheckingSomething` |
| parole | `Explain`, `Speaking`, `GestureRight`, `Announce` |
| succès | `Congratulate`, `Pleased`, `Acknowledge` |
| erreur | `Alert`, `Confused`, `DoMagic1` |
| repos | tout ce qui commence par `Idle` |
| sortie | `GoodBye`, `Goodbye`, `Hide` |

Note pour l'entrée : sur les personnages qui l'ont, `Greeting` est la vraie entrée composée
(Clippy : 39 frames, ~4 s, part de frames vides) alors que `Show` est un surgissement de
5 frames. `Greeting` d'abord, `Show` en repli — c'est pour ça que l'ordre compte.

Le repos se joue en boucle quand rien ne se passe.

## Ton périmètre exclusif

```
src/agent/**              (à créer)
src/stores/assistant.store.ts   (à créer)
src/components/Desktop.tsx      (uniquement pour monter le personnage)
src/apps/settings/**            (uniquement pour la page de choix du personnage)
```

Rien d'autre. **En particulier : rien dans `api/`** — c'est le périmètre d'AGENT-A, qui
travaille en même temps que toi. Et **rien dans `package.json`** : tout est déjà installé.

Attention à `Desktop.tsx` : tu y ajoutes le montage du personnage, tu ne touches à rien
d'autre. Le dock et le fond d'écran viennent d'y être posés.

## Le travail

### 1 · Le moteur de sprites

`src/agent/SpriteAgent.tsx`. Il empile `overlayCount` calques, chacun portant `map.png` en
fond, et fait avancer la position de fond frame par frame selon les durées. Une frame sans
`images` masque le calque.

Le nettoyage compte : un composant démonté au milieu d'une animation ne doit pas laisser un
minuteur qui tourne. Et `agent.json` ne se charge qu'à la demande — 1,3 Mo par planche, on ne
précharge pas les douze.

### 2 · Le registre

`src/agent/characters.ts` : id, nom, largeur, hauteur, chemins des deux fichiers, et deux
couleurs de bulle (fond pastel clair, contour de la même teinte tiré vers le noir).

Les dimensions réelles, mesurées dans les `agent.json` téléchargés :

```
clippy 124×93 · links 124×93 · rover 80×80 · merlin 128×128 · genie 128×128
peedy 160×128 · genius 124×93 · rocky 124×93 · f1 124×93 · officelogo 124×93
saeko 98×115 · monkeyking 124×93
```

**Le registre est le point d'extension.** Un jour on remplacera ces personnages Microsoft par
des personnages maison ; ajouter un dossier de sprites et une ligne ici doit suffire. Écris-le
en conséquence, et dis-le dans un commentaire.

### 3 · L'état

`src/stores/assistant.store.ts`, Zustand persisté : actif, personnage choisi, position,
conversation, parole activée.

**Piège de cet écosystème, quatre fois payé** : un sélecteur qui construit un objet ou un
tableau neuf à chaque appel fait boucler React — « getSnapshot should be cached », puis
« Maximum update depth exceeded », puis page blanche. Un sélecteur ne rend qu'un scalaire ou
une référence déjà stable ; toute dérivation se fait dans le composant, mémorisée.

Borne la conversation persistée (une quarantaine de messages) : `localStorage` est partagé
avec les thèmes et le fond d'écran, un dépassement de quota les emporterait tous.

### 4 · La bulle et la conversation

`src/agent/AssistantOverlay.tsx` : le personnage déplaçable, une bulle avec la réponse et un
champ de saisie. Branche `useChat` de `@ai-sdk/react` sur `/api/chat`.

L'animation suit l'état réel : réflexion pendant que ça pense, parole pendant que ça écrit,
erreur si ça échoue, repos sinon. C'est tout l'intérêt du personnage — sans ça c'est une
fenêtre de chat avec un dessin à côté.

**Si `/api/chat` ne répond pas, le personnage le dit dans sa bulle.** Pas de bulle vide, pas
de chargement éternel : une cible morte doit se voir.

### 5 · Les outils

Le serveur les déclare, **tu les exécutes**. Les cinq du contrat, sur le magasin de coquille
(`src/stores/shell.store.ts`) et le magasin CMS. `onToolCall` de `useChat` est le point
d'accroche.

Un outil qui échoue rend une erreur lisible que le modèle peut relire — pas une exception qui
casse le tour de boucle.

### 6 · Le choix du personnage

Deux endroits, comme dans RyOS :

- un menu dans la barre du haut, pour changer vite ;
- une page dans Settings, avec un aperçu de chaque personnage et les réglages
  (actif, parole, position remise à zéro).

## Preuve attendue

Des captures, dans `preuves/agent-b/`. `node tools/shot.mjs` sait poser un thème et capturer
le bureau ; pour ce qui bouge, `page.evaluate` et des captures à intervalle valent mieux qu'un
raisonnement.

Ce qu'il faut montrer :

1. le personnage sur le bureau, **trois personnages différents** dont un à 3 couches
   (Merlin, Genie ou Peedy) — c'est le cas qui casse si l'empilement est raté ;
2. l'animation d'entrée : trois captures à 0, 1 et 3 secondes, où l'on voit qu'il se
   matérialise et que la pose change ;
3. la bulle avec une vraie réponse venue de `/api/chat` ;
4. la bulle quand `/api/chat` est injoignable — le message d'erreur doit être lisible ;
5. la page Settings du personnage.

Et : `npx vitest run` reste à 60/60, aucune erreur de console.

## Rapport

Il contient les captures, la liste des fichiers créés, et une section **« ce que je n'ai pas
fait, et pourquoi »**. Si tu n'as pas pu vérifier quelque chose, dis-le — ne le maquille pas.
