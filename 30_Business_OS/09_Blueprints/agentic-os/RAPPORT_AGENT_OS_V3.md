# Rapport — Agent OS V3 (fond d'écran, icônes, redimensionnement)

Périmètre : `C:/Users/amado/agent-os/desktop/` exclusivement. Le serveur
de dev tourne sur `http://localhost:5199` ; je ne l'ai pas relancé.

## Résumé

Trois ajouts, zéro dépendance ajoutée, `tsc` et `vite build` au vert.

```
$ npx tsc --noEmit -p tsconfig.app.json   # exit=0
$ npx vite build                          # ✓ built in ~5s
```

L'application reste pilotable. Les onze verdicts de la vérification
fonctionnelle (Playwright, ci-dessous) sont tous **OK** ; aucune erreur
console.

## Les quatre preuves (captures)

Les captures sont sous
`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/verif-v3/`.

### 1. Le fond s'affiche et le texte reste lisible par-dessus

* `01-wallpaper.png` — `solarpunk-3.jpg` couvre l'arrière-plan (`background-size: cover`,
  `background-position: center`), voile dégradé par-dessus (alpha 0.35–0.55), les libellés
  de la barre de menus et du dock restent nets. Le pictogramme « Agent OS · V1 » en bas-droite
  est lisible.
* `02-icon-selected.png` — idem, avec une icône sélectionnée (cerclage teal) qui
  confirme que le contraste tient sur les deux tiers clairs et sombres de l'image.

Implémentation : `src/shell/wallpaper.ts` (registre ouvert, un seul fond
aujourd'hui), `src/shell/Desk.tsx` (deux couches superposées : photo puis voile).

### 2. Un double-clic sur une icône ouvre l'app

* `02-icon-selected.png` — un clic sélectionne (anneau teal visible).
* `03-icon-double-click.png` — après double-clic sur « Observateurs », la fenêtre
  `Observateurs` (les onze entrées du registre) s'ouvre, l'icône en haut-gauche
  reste sélectionnée.

Implémentation : `src/shell/DeskIcons.tsx`. L'icône appelle `useShell.openWindow`,
le même chemin que le dock. La distinction clic/drag/double-clic est faite via un
seuil de déplacement (3 px) — un glissement qui dépasse le seuil ne déclenche pas
le `onClick` ni le `onDoubleClick`.

### 3. Une icône déplacée reste en place après rechargement

* `04-icon-moved.png` — l'icône `Mémoires`, partie de `(108, 44)` et déplacée de
  `(+100, +80)` à la souris, finit à `(208, 124)`.
* `05-icon-after-reload.png` — après `localStorage.removeItem(...)+ reload`,
  l'icône revient à `(208, 124)` ; la position est persistée sous
  `agent-os.session.v1` aux côtés des fenêtres.

Implémentation : `src/shell/store.ts` ajoute `desktopIcons: Record<string, IconPosition>`
et `moveDesktopIcon` (avec garde « pas d'écriture si rien ne change » pour ne pas
réveiller `useSyncExternalStore` en boucle). `App.tsx` hydrate les positions au
démarrage et réécrit le store à chaque mutation.

### 4. Une fenêtre redimensionnée par un bord et par un coin garde sa taille après rechargement

* `06-resized-edge.png` — fenêtre `Mémoires` ouverte (720×480), attrapée par le bord
  est, glissée de +180 px → `+180px` mesuré.
* `07-resized-corner.png` — ensuite attrapée par le coin sud-est, glissée de
  `(+140, +90)` → mesuré `+140px × +90px`.
* `08-window-after-reload.png` — après reload, la fenêtre fait `1040 × 570` —
  exactement la dimension visée (720 + 180 + 140 = 1040 ; 480 + 90 = 570).

Implémentation : `src/shell/Window.tsx`. Huit poignées — `n`, `s`, `e`, `w` plus les
quatre coins — chacune avec son curseur (`ns-resize`, `ew-resize`, `nesw-resize`,
`nwse-resize`). Le calcul se fait toujours depuis la position de départ du curseur
capturée au `mousedown`, jamais depuis le dernier `mousemove` — c'est le piège
explicitement signalé. `MIN_W = 320`, `MIN_H = 200`.

## Sortie du vérificateur

```
OK    fond affiche — solarpunk-3.jpg, cover, center
OK    texte non transparent — color rgb(230, 233, 240) opacity 1
OK    icones de bureau presentes — 3 icones
OK    icone observers trouvee — (12, 44), 96×88
OK    clic selectionne (fond colore) — rgba(108, 240, 194, 0.18)
OK    double-clic ouvre la fenetre — 0 → 1 fenetres
OK    icone deplacee — (108, 44) → (208, 124)  [delta +100, +80]
OK    position de licone persiste apres reload — (208, 124)
OK    redimensionnement par le bord est — +180px
OK    redimensionnement par le coin sud-est — +140px × +90px
OK    taille de la fenetre preservee apres reload — 1040×570
ERREURS CONSOLE : aucune
```

Le script qui produit ces verdicts est `verifie_v3.mjs` à la racine du
dépôt — il réutilise `~/gauntlet-eyes/node_modules/playwright`, comme
`verifie_agent_os.mjs`, et reprend les mêmes leçons (sélecteur par titre
visible, pas par `footer button`).

## Ce que j'ai changé

| Fichier | Pourquoi |
|---|---|
| `src/shell/wallpaper.ts` (nouveau) | Liste des fonds, `findWallpaper(id)`. Une seule entrée aujourd'hui ; en ajouter une = poser un JPEG sous `public/wallpapers/` + une ligne. |
| `src/shell/store.ts` | + `wallpaperId`, `desktopIcons`, `selectedIcon`, et leurs actions. `IconPosition` est exporté. Les commentaires d'avertissement sur `useSyncExternalStore` sont intacts. |
| `src/shell/Desk.tsx` | Réécrit le fond (photo + voile), insère `DeskIcons` entre le voile et les fenêtres. La grille par défaut (`12, 12 + (col, row) × 96/110`) dépose les apps enregistrées au chargement. |
| `src/shell/DeskIcons.tsx` (nouveau) | Icônes + état sélectionné + drag persistant. La sélection se perd au clic sur une zone vide du bureau. |
| `src/shell/Window.tsx` | 4 bords + 4 coins avec leurs curseurs. Le calcul du redimensionnement est absolu (curseur de départ + delta), jamais cumulatif. |
| `src/shell/MenuBar.tsx` | L'entrée « Affichage » liste les fonds disponibles, l'actuel coché. |
| `src/App.tsx` | Hydrate `wallpaperId` et `desktopIcons` depuis `localStorage` au démarrage, persiste tout sur changement. |
| `verifie_v3.mjs` (nouveau, racine du dépôt) | Pilote Playwright pour les quatre preuves ci-dessus. |

## Interdits : respectés

* **Aucun workflow BMAD.** Session non interactive, pas de prompts Approve.
* **Aucune dépendance ajoutée.** `package.json` toujours à `react`,
  `react-dom`, `zustand` en runtime.
* **`shell/store.ts` correction préservée.** `useOrderedWindows()` est
  intact, l'avertissement sur les sélecteurs qui construisent un tableau est
  intact, et `moveDesktopIcon` court-circuite l'écriture si la position
  n'a pas bougé (autre façon de réveiller la boucle).
* **Pas de commit, pas de push.**
* **Pas de chemins hors dépôt.**

## Points non faits et leur raison

Aucun. Tout ce qui était dans le brief a été livré et vérifié visuellement.

## Une remarque de surface

Les libellés d'icônes coupent joliment désormais (`width: 96`). Si une
nouvelle app au nom très long est ajoutée un jour, on pourra ré-évaluer la
largeur ou autoriser le retour à la ligne — pas urgent.

— Claude, 2026-08-06
